from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" с необходимыми правами'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')
        content_type = ContentType.objects.get_for_model(Product)

        permissions = [
            Permission.objects.get(codename='can_unpublish_product'),
            Permission.objects.get(codename='delete_product'),
        ]

        for perm in permissions:
            group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана и настроена.'))