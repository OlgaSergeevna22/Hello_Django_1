from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = '72926ea7ea0ca4e5887ebbe9834ba023'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()



    cities = City.objects.all()
    all_cities=[]
    hist_cities = []



    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city':city.name,
            'temp':res['main']['temp'],
            'icon':res['weather'][0]['icon'],
            'speed': res['wind']['speed'],
            'cloud': res['clouds']['all']
    }
        hist_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'speed': res['wind']['speed'],
            'cloud': res['clouds']['all']
        }

        hist_cities.append(hist_info)


    all_cities.append(city_info)


    context = {'all_info':all_cities, 'hist_info':hist_cities, 'form':form}
    return render(request, 'weather/index.html', context)





def My_templ(request):
    appid = '72926ea7ea0ca4e5887ebbe9834ba023'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city)).json()
    city_info = {
        'city':city.name,
        'temp':res['main']['temp'],
        'icon':res['weather'][0]['icon'],
        'speed':res['wind']['speed'],
        'cloud':res['clouds']['all']
    }

    all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/My_templ.html', context)



