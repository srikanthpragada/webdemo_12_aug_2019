from django.shortcuts import render
from .models import Book
from django.db.models import Avg, Count

def books_home(request):
    details = Book.objects.all().aggregate(average = Avg('price'), count = Count('id'))
    return render(request, 'books_home.html', {'details' : details })


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books' : books })
