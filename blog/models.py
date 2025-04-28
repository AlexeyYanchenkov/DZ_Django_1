from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='URL')
    content = models.TextField(verbose_name='Контент')
    preview = models.ImageField(upload_to='blog_previews/', verbose_name='Превью', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return self.title