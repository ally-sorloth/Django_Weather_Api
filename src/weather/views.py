from django.shortcuts import redirect, render
from decouple import config
import requests
from pprint import pprint

from .forms import CityForm
from .models import City
from django.contrib import messages

def index(request):
    form = CityForm()
    cities = City.objects.all()
    url = config("BASE_URL")
    
    
    # print(type(a))
    # pprint(content)
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data["name"]
            if not City.objects.filter(name=new_city).exists():
                form.save()
            else:
                messages.warning(request, "City already exists")
            return redirect("home")
    
    city_data = []
    for city in cities: 
        # print(city)
        r = requests.get(url.format(city))
        content = r.json()
        
        weather_data = {
            "city": city.name,
            "temp": content["main"]["temp"],
            "description": content["weather"][0]["description"],
            "icon": content["weather"][0]["icon"]
        }
        
        city_data.append(weather_data)
    # print(city_data)
        
    context = {
        "city_data": city_data,
        "form": form
    }
    return render(request, "weather/index.html", context)

# Create your views here.
