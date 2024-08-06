from .views import index, about
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('', about, name='about'),
]