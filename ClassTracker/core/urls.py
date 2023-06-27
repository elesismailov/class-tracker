
from django.urls import path
from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('classrooms/<str:id>/', classrooms_by_id, name='classrooms-by-id'),
    path('classrooms-all/', classrooms_list, name='classrooms-all'),

    path('students/', students_list, name='students'),
    path('students/<str:id>/', students_by_id, name='students-by-id'),

    path('sign-up/', sign_up, name='sign-up'),
    path('log-in/', log_in, name='log-in'),
    path('log-out/', log_out, name='log-out'),
]
