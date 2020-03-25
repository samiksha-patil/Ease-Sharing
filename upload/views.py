from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def book_list(request):
    books=Book.objects.all()
    query=request.GET.get("q")
    if query :
        books= books.filter(
            Q(title__icontains=query)|
            Q(author__icontains=query)
            ).distinct()    
    return render(request,'book_list.html',{
        'books':books
        })
def upload_book(request):
    if request.method=='POST':
        form=BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'upload_book.html',{
        'form':form
        })
