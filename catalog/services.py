from .models import Product
from django.core.cache import cache

def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id, is_published=True)

def get_all_products_cached():
    cache_key = 'all_products'
    products = cache.get('all_products')

    if products is None:
        print('Производится запрос...')
        products = Product.objects.filter(is_published=True)
        cache.set(cache_key, products, 60 * 10)

    return products