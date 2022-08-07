from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email, email_token):
    subject = 'Your account needs to be verified' 
    email_from = settings.EMAIL_HOST_USER
    messages = f'Please click on the link below to verify your account \n http://127.0.0.1:8000/accounts/activate/{email_token}'
    send_mail(subject, messages, email_from, [email], fail_silently=False)
    