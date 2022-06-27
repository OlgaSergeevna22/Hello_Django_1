from django.shortcuts import render
import requests

def index(request):
    appid = '72926ea7ea0ca4e5887ebbe9834ba023'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid


    city = 'Brest'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city':city,
        'temp':res['main']['temp'],
        'icon':res['weather'][0]['icon']
    }
    context = {'info':city_info}
    return render(request, 'weather/index.html', context)


def My_templ(request):
    appid = '72926ea7ea0ca4e5887ebbe9834ba023'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid


    city = 'Brest'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city':city,
        'temp':res['main']['temp'],
        'icon':res['weather'][0]['icon'],
        'speed':res['wind']['speed'],
        'cloud':res['clouds']['all']
    }
    context = {'info':city_info}
    return render(request, 'weather/My_templ.html', context)


