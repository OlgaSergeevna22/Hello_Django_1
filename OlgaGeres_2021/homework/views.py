from django.shortcuts import render

def homework(request):
    return render (request,'home_1.html')

def main_page(request):
    return render (request,'main_page.html')
