from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from books.models import Book
from datetime import datetime

@login_required
def home(request):

    if request.method == "POST":
        if request.user.is_authenticated:
            book_name = request.POST.get("book_name")
            book_author = request.POST.get("author_name")
            # publish_date = request.POST.get("published_date")
            publish_date_str = request.POST.get("published_date")
            price = request.POST.get("book_price")

            # Check if the publish_date is empty or invalid
            publish_date = None
            if publish_date_str:
                try:
                    publish_date = datetime.strptime(publish_date_str, "%Y-%m-%d").date()
                except ValueError:
                    publish_date = None  # Set to None if invalid date


            book = Book.objects.create(
                book_name = book_name,
                author_name = book_author, 
                publish_date = publish_date, 
                book_price = price
                )
            book.save() 
        else:
            return redirect('login')    

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {'title' : 'About'})

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books' : books})

@login_required
def update_book(request, id):
    book = get_object_or_404(Book, id = id)

    print('bookIs', book.publish_date)

    if request.method == "POST":
        book.book_name = request.POST.get("book_name")
        book.author_name = request.POST.get("author_name")
        print(request.POST.get("published_date"))
        book.publish_date = request.POST.get("published_date")
        book.book_price = request.POST.get("book_price")

        book.save() 

        return redirect('book_list')
    
    return render(request, 'update_book.html', {'book' : book})

@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, id = id)
    book.delete()
    return redirect('book_list')