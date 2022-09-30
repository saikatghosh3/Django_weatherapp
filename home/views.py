from django.shortcuts import render
import requests
# Create your views here.
def home(request):

    city= request.GET.get('city',"dhaka")
    urls=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d0d0ce78b02e1842d7fc3045e72d1644'
    data= requests.get(urls).json()
    print(data)

    payload={
        'city' : data['name'],
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],
        'kenvin_temperature': data['main']['temp'],
        'celcius_temperature': int(data['main']['temp'] -273),
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description'],
    }


    context={'data': payload }
    print(context) 
    return render(request,'home.html',context)