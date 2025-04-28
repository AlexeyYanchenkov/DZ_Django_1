from django.urls import path
from .views import HomePageView, ProductDetailView, ContactsView

app_name = 'catalog'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]