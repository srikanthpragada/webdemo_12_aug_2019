from django.shortcuts import render
from django.http import HttpResponse
import datetime


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def get_date_time(request):
    now = datetime.datetime.now()
    return HttpResponse(str(now))
