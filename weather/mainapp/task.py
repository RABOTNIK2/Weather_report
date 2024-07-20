from celery import shared_task

from .models import *

@shared_task
def save_request(city_name):
    try:
        city = City.objects.get(name__icontains=city_name)
        city.quantity +=1
        city.save()
    except City.DoesNotExist:
        new_city = City.objects.create(name=city_name, quantity=1)
        new_city.save()