from django.urls import path 
from . import views
urlpatterns = [

    path('',views.index , name = 'home'),
    path('books/',views.books , name = 'books'),

    path('update/<int:id>',views.updatebook, name="update"),

    path('delete/<int:id>',views.deletebook, name="delete"),

    path('nn/',views.BooksView.as_view() , name = 'nn'),



]