from re import template
from django.shortcuts import redirect, render
from django.urls import reverse
import pkg_resources

from MyApp.form import AuthorForm, BookForm, MemoryForm
from django.views import generic
from MyApp.models import Author, Book, Memory


# 登録したデータ一覧を表示するview
def index(request):
    book_list = Book.object.all()
    return render(request, "MyApp/index.html", {"book_list":book_list})

# それぞれの本について詳細を表示するview
def bookdetail(request, pk):
    book_detail = Book.object.get(pk = pk)
    return render(request, "MyApp/detail.html", {"book_detail":book_detail})

# 作者名を登録するview
def registerauthor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit = False)
            author.save()
            return redirect('myapp:registerbook')
    else:
        form = AuthorForm()
        return render(request, 'myapp/register.html', {'form': form})

# 本の情報を登録するview
def registerbook(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            book = form.save(commit = False)
            book.save()
            return redirect('myapp:book_detail', pk = book.pk)
    else:
        form = BookForm()
        return render(request, 'myapp/register.html', {'form': form})

# 本の感想を登録するview
def writingmemory(request):
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.save()
            return redirect('myapp:book_detail', pk=memory.book.pk)
    else:
        form = MemoryForm()
        return render(request, 'myapp/register.html', {'form': form})
