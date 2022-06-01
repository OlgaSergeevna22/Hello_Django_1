from django.shortcuts import render
from .models import Project

def project_index (request):
    projects = Project.objects.all()

def func(request):
    return render(request,'index.html')
# Create your views here.
