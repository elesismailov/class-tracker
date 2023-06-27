from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

def notify_email(emails, subject, body):
    print('sending emails...')
    send_mail(
        subject        = subject,
        message        = body,
        from_email     = settings.EMAIL_HOST_USER,
        auth_user      = settings.EMAIL_HOST_USER,
        auth_password  = settings.EMAIL_HOST_PASSWORD,
        recipient_list = emails,
        fail_silently  = True,
        )