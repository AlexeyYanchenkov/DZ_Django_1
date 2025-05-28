from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} <{self.email}>"

class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject

class Mailing(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('finished', 'Завершена'),
    ]

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Client)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mailings')

    def __str__(self):
        return f"Рассылка #{self.id} — {self.get_status_display()}"

    def success_attempts_count(self):
        return self.attempts.filter(status='success').count()

    def failed_attempts_count(self):
        return self.attempts.filter(status='failed').count()

    def total_messages_sent(self):
        return self.attempts.count()

class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ('success', 'Успешно'),
        ('failed', 'Не успешно'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    server_response = models.TextField()
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='attempts')

    def __str__(self):
        return f"{self.mailing} — {self.get_status_display()} ({self.timestamp})"