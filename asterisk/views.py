from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'asterisk/home.html')


def get_logs_view(request):
    return render(request, 'asterisk/get_logs.html')
