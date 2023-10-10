from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg, Max, Min


def home(request):
  books = Book.objects.all().order_by("-rating") #.values() to print
  
  num_books = books.count()
  avg_rating = books.aggregate(Avg("rating")) # rating__avg, rating__min

  return render(request, 'book/home.html', { 
    "books": books,
    "total_number_of_books": num_books,
    "average_rating": avg_rating['rating__avg'],
  })


def details(request, slug):
  book = get_object_or_404(Book, slug=slug)
  return render(request, 'book/details.html', {
    "title": book.title,
    "author": book.author,
    "rating": book.rating,
    "is_bestseller": book.is_bestselling
  })

  # try:
  #   book = Book.objects.get(id=slug)
  # except:
  #   raise Http404()
