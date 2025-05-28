from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from mailing.models import Mailing

class Command(BaseCommand):
    help = 'Создание групп Пользователь и Менеджер с соответствующими правами'

    def handle(self, *args, **options):
        user_group, created = Group.objects.get_or_create(name='Пользователь')
        manager_group, created = Group.objects.get_or_create(name='Менеджер')

        mailing_ct = ContentType.objects.get_for_model(Mailing)

        # Права для Менеджера
        permissions = Permission.objects.filter(content_type=mailing_ct)
        manager_group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS('Группы и права успешно созданы'))