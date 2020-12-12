from django.shortcuts import render, redirect
from . models import *

def index(request):
    context = {
        'display_books': Book.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['description'],
    )
    return redirect('/')
def author(request):
    context = {
        'display_author': Author.objects.all()
    }
    return render(request, 'author.html', context)

def add_author(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
    )
    return redirect('/author')

def view_book(request):
    context = {}

def author_page(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        'author': author,
        'authors_books' : author.books.all(),
        'all_books': Book.objects.all(),
    }
    return render(request, 'author_page.html', context)


def book_page(request, book_id):
    book = Book.objects.get(id=book_id)
    book_authors = book.authors.all()
    all_authors = Author.objects.all()
    for author_book in book_authors:
        all_authors = all_authors.exclude(id=author_book.id) 
    context = {
        'book': book,
        'book_authors': book_authors,
        'all_authors': all_authors,
    }
    return render(request, 'book_page.html', context)

def assign_author(request):
    book = Book.objects.get(id= request.POST['book_id'])
    assign_author = Author.objects.get(id = request.POST['Authors'])
    book.authors.add(assign_author)
    return redirect(f'/book/{book.id}') 

def assign_book(request):
    author = Author.objects.get(id= request.POST['author_id'])
    assign_book = Book.objects.get(id = request.POST['books'])
    author.books.add(assign_book)
    return redirect(f'/author/{author.id}') 
