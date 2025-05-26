from django.urls import path
from .views import CategoryProductListView, HomePageView, ProductDetailView, ContactsView, ProductListView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products_list/', ProductListView.as_view(), name='products_list'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', CategoryProductListView.as_view(), name='products_by_category'),
]
