from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .forms import BookForm
from .models import Book


def listBooks(request):
    books = Book.objects.all()
    return render(request, "books/list-books.html", {
        "books": books
    })


def addBook(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.title = book.title.title()
            book.save()
            messages.success(request, "Novo livro adicionado com sucesso.")
            return redirect("add-book")

    return render(request, "books/book-form.html", {
        "form": form
    })
