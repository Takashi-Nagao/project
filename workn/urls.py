from django.urls import path
from .import views

app_name = 'workn'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.add, name='add'),
]