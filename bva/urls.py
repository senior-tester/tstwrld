from django.urls import path
from . import views

app_name = 'bva'
urlpatterns = [
    path('', views.index, name='index'),
]