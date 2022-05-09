from re import template
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
import pkg_resources

from MyApp.form import AuthorForm, BookForm, MemoryForm
from MyApp.models import Author, Book, Memory



def index(request):
    book_list = Book.objects.all()
    return render(request, "MyApp/index.html", {"book_list": book_list})


def bookdetail(request: HttpRequest, pk):
    book_detail = Book.objects.get(pk=pk)
    return render(request, "MyApp/detail.html", {"book": book_detail})


def registerauthor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('MyApp:registerbook')
    else:
        form = AuthorForm()
        return render(request, 'MyApp/register.html', {'form': form})


def registerbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            tempbook = form.save(commit=False)
            tempbook.save()
            return redirect('MyApp:book_detail', pk = tempbook.pk)
    else:
        form = BookForm()
        return render(request, 'MyApp/register.html', {'form': form})


def writingmemory(request, pk):
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            tempmemory = form.save(commit=False)
            tempmemory.save()
            return redirect('MyApp:book_detail', pk = tempmemory.title.pk)
    else:
        form = MemoryForm()
        return render(request, 'MyApp/register.html', {'form': form})


def updatememory(request, pk):
    obj = get_object_or_404(Memory, id=pk)
    if request.method == "post":
        form = MemoryForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('MyApp:book_detail', pk=obj.title.pk)
    else:
        form = MemoryForm(instance=obj)
        return render(request, 'MyApp/register.html', {'form': form})


def writingthisbookmemory(request, book_id):
    obj = get_object_or_404(Book, id=book_id)
    form = MemoryForm({'book': obj})
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.save()
            return redirect('MyApp:book_detail', pk=memory.obj.pk)
    else:
        return render(request, 'MyApp/register.html', {'form': form})


def deletememory(request, pk):
    obj = get_object_or_404(Memory, id=pk)
    book_id = obj.title.pk
    if request.method == "POST":
        obj.delete()
        return redirect('MyApp:book_detail', pk=book_id)
    return render(request, "MyApp/delete.html", {'obj': obj})


def deletebook(request, pk):
    obj = get_object_or_404(Book, id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('MyApp:index')
    context = {'obj': obj}
    return render(request, "MyApp/delete.html", context)
