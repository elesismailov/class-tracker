
from django.urls import path
from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('students/', students_list, name='students'),

    path('sign-up/', sign_up, name='sign-up'),
    path('log-in/', log_in, name='log-in'),
    path('log-out/', log_out, name='log-out'),
]