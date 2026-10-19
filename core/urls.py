from django.urls import path
from django.views.generic import RedirectView

app_name = 'core'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='bva:index', permanent=False), name='index'),
]