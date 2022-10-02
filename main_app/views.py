# Imports
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Home View
def home(request):
  return HttpResponse('<h1>Vita Home Page</h1>')