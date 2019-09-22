from django.shortcuts import render
from .forms import UpdateAuthorForm
import requests
import sqlite3
from django.http import HttpResponse


def welcome(request):
    topics = ['Template', 'Forms', 'ORM', 'Rest API']
    return render(request, 'welcome.html', {'topics': topics})


def update_author(request):
    if request.method == "GET":
        f = UpdateAuthorForm()
        return render(request, 'update_author.html', {'form': f})
    else:
        f = UpdateAuthorForm(request.POST) # copy data from HTML fields to form
        if f.is_valid():
            id = f.cleaned_data['id']
            email = f.cleaned_data['email']
            # update database
            con = None
            try:
                con = sqlite3.connect(r"e:\classroom\python\aug12\catalog.db")
                cur = con.cursor()
                cur.execute("update authors set email = ? where id = ?",
                            (email,id))
                if cur.rowcount == 1:
                   message  = "Updated Successfully!"
                   con.commit()
                else:
                   message = "Invalid Author Id!"
            except Exception as ex:
                message = "Could not update author due to error!"
            finally:
                if con is not None:
                    con.close()

        else:
            message =""   #"Sorry! Invalid data. Please resubmit with valid data!"

        return render(request, 'update_author.html',
                      {'form': f, 'message' : message})



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
                          {
                              'message': 'Sorry! Could not add author. Please correct and resubmit!',
                              'aname': name,
                              'email': email,
                              'phone': phone
                          }
                          )
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
