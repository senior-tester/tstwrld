from django.shortcuts import render


def index(request):
    return render(request, 'bva/index.html')