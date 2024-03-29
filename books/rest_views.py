from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'publisher', 'price')


def client(request):
    return render(request, 'rest_client.html')


@api_view(['GET','POST'])
def process_books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else: # Post
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()  # insert into table
            return Response(book.data)
        else:
            return Response(book.errors, status=400)  # bad request


@api_view(['GET','DELETE'])
def process_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except:
        return Response(status=404)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    else:  # DELETE
        book.delete()
        return Response(status=204)  # No data

