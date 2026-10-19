from django.urls import path
from . import views

app_name = 'dirty_strings'
urlpatterns = [
    path('', views.index, name='index'),
]