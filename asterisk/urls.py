from django.urls import path
from .views import home, get_logs_view, dialplan_details_view

app_name = 'asterisk'

urlpatterns = [
    path('', home, name='home'),
    path('get-logs/', get_logs_view, name='get_logs'),
    path('detail-dialplan/', dialplan_details_view, name='detail_dialplan'),
]
