from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book
from django.db.models import Avg, Count
from .forms import BookForm


def books_home(request):
    details = Book.objects.all().aggregate(average=Avg('price'), count=Count('id'))
    return render(request, 'books_home.html', {'details': details})


def books_search(request):
    return render(request,'books_search.html')

def books_search_books(request):
    title = request.GET['title']
    books = Book.objects.filter(title__contains=title)
    books = list(books.values())  # Convert Book to dict and then QuerySet to list
    return JsonResponse(books, safe=False)


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})


def books_add(request):
    if request.method == "GET":
        f = BookForm()
        return render(request, 'books_add.html', {'form': f})
    else:  # post
        f = BookForm(request.POST)
        if f.is_valid():
            f.save()
            message = f"Book [{f.cleaned_data['title']}] has been added successfully"
            f = BookForm()
        else:
            message = ""

        return render(request, 'books_add.html',
                      {'form': f, 'message': message})


def books_delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/books/list")


def books_edit(request, id):
    try:
        book = Book.objects.get(id=id)
    except:
        return render(request, 'books_edit.html',
                      {'message': 'Invalid Book ID'})

    if request.method == "GET":
        f = BookForm(instance=book)
        return render(request, 'books_edit.html', {'form': f})
    else:  # post
        f = BookForm(instance=book, data=request.POST)
        if f.is_valid():
            f.save()
            return redirect("/books/list")
        else:
            return render(request, 'books_edit.html', {'form': f})
