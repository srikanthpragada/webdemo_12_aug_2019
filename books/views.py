from django.shortcuts import render
import requests
from django.http import HttpResponse


def welcome(request):
    topics = ['Template', 'Forms', 'ORM', 'Rest API']
    return render(request, 'welcome.html', {'topics': topics})


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    countries = sorted(countries,key=lambda c : c['population'], reverse=True)[:10]
    return render(request, 'countries.html',
                  {'countries': countries })
