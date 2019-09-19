from django.http import HttpResponse


def welcome(request):
    return HttpResponse("<h1>Welcome To Django</h1>")
