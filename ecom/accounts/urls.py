from django.urls import path
from .views import activate_email, login_page,register_page
# logout_page, profile_page

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('activate/<email_token>/', activate_email, name='activate_email'),
]
