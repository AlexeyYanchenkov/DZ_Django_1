from pathlib import Path

from django.core.management import BaseCommand

from catalog.models import Category, Product
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories() -> list:
        """
        Получение данных из фикстуры с категориями
        :return: список с категориями
        """
        with open(Path(__file__).parent.parent.parent.parent.joinpath("catalog_fixture.json"), encoding="utf-8") as file:
            values = json.load(file)
        categories = [value for value in values if value['model'] == "catalog.category"]
        return categories

    @staticmethod
    def json_read_products() -> list:
        """
        Получение данных из фикстуры с продуктами
        :return: список с продуктами
        """
        with open(Path(__file__).parent.parent.parent.parent.joinpath("catalog_fixture.json"), encoding="utf-8") as file:
            values = json.load(file)
        products = [value for value in values if value['model'] == "catalog.product"]
        return products

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category({"id": category['pk'], "name": category['fields']['name'],
                          "description": category['fields']['description']})
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product({"id": product['pk'], "name": product['fields']['name'],
                         "description": product['fields']['description'],
                         "price": product['fields']['price'],
                         "category": Category.objects.get(pk=product['fields']['category']),
                         "image": product['fields']['image'], "created_at": product['fields']['created_at'],
                         "updated_at": product['fields']['updated_at']})
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
        Category.objects.bulk_create(category_for_create)