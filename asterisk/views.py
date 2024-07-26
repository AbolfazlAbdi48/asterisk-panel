from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'asterisk/home.html')


def get_logs_view(request):
    return render(request, 'asterisk/get_logs.html')


def dialplan_details_view(request):
    return render(request, 'asterisk/dialplan_details.html')


def create_channel_view(request):
    return render(request, 'asterisk/create_channel.html')
