from django.views.generic import ListView, TemplateView
from .models import Client, Message, Mailing
from django.core.mail import send_mail
from django.conf import settings

def send_mailing(mailing):
    for client in mailing.recipients.all():
        try:
            send_mail(
                mailing.message.subject,
                mailing.message.body,
                settings.DEFAULT_FROM_EMAIL,
                [client.email],
                fail_silently=False,
            )
            # Сохрани успешную попытку
        except Exception as e:
            # Сохрани неуспешную попытку
            pass

class MailingStatsView(TemplateView):
    template_name = "mailing/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_mailings'] = Mailing.objects.count()
        context['active_mailings'] = Mailing.objects.filter(status='Запущена').count()
        context['unique_clients'] = Client.objects.count()
        return context

class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'

class MessageListView(ListView):
    model = Message
    template_name = 'mailing/message_list.html'

class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'