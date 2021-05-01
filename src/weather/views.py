from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint

def index(request):
    url = config("BASE_URL")
    city = "Berlin"
    r = requests.get(url.format(city))
    content = r.json()
    # print(type(a))
    # pprint(a)
    context = {
        "city": city,
        "temp": content["main"]["temp"],
        "description": content["weather"][0]["description"],
        "icon": content["weather"][0]["icon"]
    }
    return render(request, "weather/index.html", context)

# Create your views here.
