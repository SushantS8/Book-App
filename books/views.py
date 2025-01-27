from django.shortcuts import render, redirect
from books.models import Book


def home(request):

    if request.method == "POST":
        book_name = request.POST.get("book_name")
        book_author = request.POST.get("author_name")
        publish_date = request.POST.get("published_date")
        price = request.POST.get("book_price")

        book = Book.objects.create(book_name = book_name, author_name = book_author, publish_date = publish_date, book_price = price)
        book.save() 

    # elif request.method == 'GET' and 'list-books' in request.GET:
    #     books = Book.objects.all() 

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {'title' : 'About'})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books' : books})

def update_book(request, id):
    book = Book.objects.get(id = id)

    print('bookIs', book.publish_date)

    # book.publish_date = book.publish_date.strftime('%d-%m-%Y')

    if request.method == "POST":
        book.book_name = request.POST.get("book_name")
        book.author_name = request.POST.get("author_name")
        print(request.POST.get("published_date"))
        book.publish_date = request.POST.get("published_date")
        book.book_price = request.POST.get("book_price")

        book.save() 

        return redirect('book_list')
    
    return render(request, 'update_book.html', {'book' : book})


def delete_book(request, id):
    book = Book.objects.get(id = id)
    book.delete()
    return redirect('book_list')