from django.shortcuts import render


def index(request):
    return render(request, 'dirty_strings/index.html')