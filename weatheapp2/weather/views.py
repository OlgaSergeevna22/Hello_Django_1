from django.shortcuts import render
import requests

def index(request):
    appid = '72926ea7ea0ca4e5887ebbe9834ba023'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid='+appid


    city = 'London'
    return render(request, 'weather/index.html')


