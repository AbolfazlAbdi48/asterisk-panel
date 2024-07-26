from django.urls import path
from .views import home, get_logs_view

app_name = 'asterisk'

urlpatterns = [
    path('', home, name='home'),
    path('get_logs/', get_logs_view, name='get_logs'),
]
