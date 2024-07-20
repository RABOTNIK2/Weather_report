from django.shortcuts import render
from django.views.generic import View
from datetime import datetime
import requests
import json
from .task import save_request
from .models import City

class IndexView(View):
    template_name = 'mainapp/home.html'
    queryset = City.objects.all()

    def get(self, request):
        city_weather = {}
        context = {'city_weather': city_weather}
        return render(request, self.template_name, context)
    
    def post(self, request):
        try:
            API_KEY = '0eeab5a6f4eeb842ffeb19c2edb3945d'
            city_name = request.POST.get('city')
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
            response = requests.get(url).json()
            current_time = datetime.now()
            save_request.delay(city_name)
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            city_weather = {
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }
            query = City.objects.all()
            context = {'city_weather': city_weather, 'requests': query}
            return render(request, self.template_name, context)
        except:
            return render(request, 'mainapp/404.html')
# Create your views here.
