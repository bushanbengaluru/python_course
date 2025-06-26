from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def firstview(request):
    return HttpResponse("<h1>Hello word</h1>")