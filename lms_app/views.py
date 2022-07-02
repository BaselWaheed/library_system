from django.shortcuts import redirect, render , get_object_or_404
from django.views.generic import ListView
from .models import Book, Category
from .forms import BookForm , CategoryForm
# Create your views here.
def index(request):
    if request.method =="POST":
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
            return redirect('books')
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context ={
        'books':Book.objects.all(),
        'category' :Category.objects.all(),
        'bookform': BookForm(),
        'categoryform': CategoryForm(),
        'allbooks' :Book.objects.filter(active=True).count(),
        'available' :Book.objects.filter(status="available").count(),
        'soled' :Book.objects.filter(status="soled").count(),
        'rented' :Book.objects.filter(status="rented").count(),
    }
    return render(request, 'lms_app/index.html',context)


def books(request):
    search =Book.objects.all()
    title = None 
    if "search_name" in request.GET :
        title = request.GET['search_name']
        if title :
            search = Book.objects.filter(title__icontains=title)



    context ={
        'books':search,
        'category' :Category.objects.all(),
        'categoryform': CategoryForm(),
    }

    return render(request, 'lms_app/books.html',context)



class BooksView(ListView):
    template_name = 'lms_app/books.html'
  


def updatebook(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == "POST":
        Form = BookForm(request.POST , request.FILES , instance=book_id)
        if Form.is_valid():
            Form.save()
            return redirect('home')
    else :
        Form = BookForm(instance=book_id)

    context = {
        "form": Form
    }
    return render(request,'lms_app/update.html' ,context)



def deletebook(request , id ):
    book_id = get_object_or_404(Book,id=id)
    if request.method =="POST":
        book_id.delete()
        return redirect('/')
    return render(request,'lms_app/delete.html')



