from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def upload(request):
    return render(request, 'upload.html')