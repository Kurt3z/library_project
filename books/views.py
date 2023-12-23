from django.shortcuts import render
from django.http import HttpResponse

from .forms import BookForm


def listBooks(request):
    return HttpResponse("List all Library Books")


def addBook(request):
    form = BookForm()

    return render(request, "books/book-form.html", {
        "form": form
    })
