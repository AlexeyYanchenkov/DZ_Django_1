from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .services import get_products_by_category
from catalog.services import get_all_products_cached

class CategoryProductListView(ListView):
    template_name = "catalog/products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        return get_products_by_category(self.kwargs['category_id'])


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm('catalog.delete_product')

class HomePageView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

#@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products_list'

    def get_queryset(self):
        return get_products_by_category()
