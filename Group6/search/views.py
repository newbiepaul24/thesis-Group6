from django.shortcuts import render
from django.http import HttpResponse
from .models import Name
# Create your views here.

def index(request):
    name = Name.objects.all()
    return render(request, 'index.html', {'name': name})