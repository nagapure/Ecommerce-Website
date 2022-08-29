from django.urls import path

from product.views import add_to_cart
from .views import activate_email, login_page,register_page
# logout_page, profile_page

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('activate/<email_token>/', activate_email, name='activate_email'),
    # path('/cart/', cart, name='add_to_cart'),
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),

]
