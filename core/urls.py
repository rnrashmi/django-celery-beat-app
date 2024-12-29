from django.urls import path
from core import views

urlpatterns = [
    path('task/', views.excute_task, name='task'),
]