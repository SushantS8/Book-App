from django.urls import path
from . import views
from .views import book_list, update_book, delete_book, home, about
from .api_views import BookListCreateView, BookDetailView


urlpatterns = [
    path('', views.home, name='books-home'),
    path('about/', views.about, name="books-about"),
    path('book-list/', views.book_list, name="book_list"),
    path('update-book/<int:id>/', views.update_book, name="update_book"),
    path('delete-book/<int:id>/', views.delete_book, name="delete_book"),

    # API views (for RESTful access)
    path('api/books/', BookListCreateView.as_view(), name='api-book-list'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='api-book-detail'),
]