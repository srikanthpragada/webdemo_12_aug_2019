from django.shortcuts import render
import requests
import sqlite3
from django.http import HttpResponse


def welcome(request):
    topics = ['Template', 'Forms', 'ORM', 'Rest API']
    return render(request, 'welcome.html', {'topics': topics})


def add_author(request):
    if request.method == "POST":
        # insert data into table as a row
        name = request.POST['aname']
        email = request.POST['email']
        phone = request.POST['phone']
        print(name, email, phone)
        con = None
        try:
            con = sqlite3.connect(r"e:\classroom\python\aug12\catalog.db")
            cur = con.cursor()
            cur.execute("insert into authors(name,email,phone) values (?,?,?)",
                        (name, email, phone))
            con.commit()
            return render(request, 'add_author.html',
                          {'message': 'Successfully added author!'})
        except Exception as ex:
            print(ex)
            return render(request, 'add_author.html',
                          {'message': 'Sorry! Could not add author'})
        finally:
            if con is not None:
                con.close()
    else:  # GET request
        return render(request, 'add_author.html')


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    countries = sorted(countries, key=lambda c: c['population'], reverse=True)[:10]
    return render(request, 'countries.html',
                  {'countries': countries})
