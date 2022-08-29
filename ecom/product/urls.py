from django.urls import path
from .views import  get_products
# logout_page, profile_page

urlpatterns = [
    path('<slug>/', get_products, name='get_product'),
]
