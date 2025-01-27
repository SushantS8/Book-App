from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books-home'),
    path('about/', views.about, name="books-about"),
    path('book-list/', views.book_list, name="book_list"),
    path('update-book/<int:id>/', views.update_book, name="update_book"),
    path('delete-book/<int:id>/', views.delete_book, name="delete_book"),
]