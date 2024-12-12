from django.shortcuts import render , redirect ,  get_object_or_404
from django.http import HttpResponse
from.models import Book , Post


def home(request):
    return render(request , 'index.html')

def book_list(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request , 'book_list.html' , context)

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request , 'posts.html' , context)

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        price = request.POST.get('price')
        book = Book.objects.create(
            title=title, 
            author=author, 
            publication_date=published_date,
            price=price

        )
        book.save()
        return redirect("book_list")
    return render(request , "add_book.html")

def book_detail(request , pk):
    book_detail = Book.objects.get(pk = pk)
    context = {
        'book': book_detail
    }
    return render(request , 'book_detail.html' , context)

def book_update(request , pk):
    book = get_object_or_404(Book , pk = pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_date = request.POST.get('published_date')
        book.price = request.POST.get('price')
        book.save()
        return redirect('book_list')
    context = {
        'book' : book
    }
    return render(request , 'book_update.html' , context)


def book_delete(request , pk):
    book = get_object_or_404(Book , pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request , 'book_delete.html')