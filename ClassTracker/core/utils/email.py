from django.core.mail import send_mail
from django.conf import settings

def notify_student(student, subject, body):
    print('sending email to ' + student.email)
    send_mail(
        subject        = subject,
        message        = body,
        from_email     = settings.EMAIL_HOST_USER,
        auth_user      = settings.EMAIL_HOST_USER,
        auth_password  = settings.EMAIL_HOST_PASSWORD,
        recipient_list = [student.email],
        fail_silently  = True,
        )