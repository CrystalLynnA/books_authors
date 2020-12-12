from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('add_book', views.add_book),
    path('author', views.author),
    path('add_author', views.add_author),
    path('author/<int:author_id>', views.author_page),
    path('book/<int:book_id>', views.book_page),
    path('book/assign_author', views.assign_author),
    path('author/assign_book', views.assign_book)
]