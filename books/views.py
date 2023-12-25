from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from .forms import BookForm, AuthorForm
from .models import Book


# Helper Functions
def is_librarian(user):
    return user.is_authenticated and user.contact.is_librarian


def listBooks(request):
    books = Book.objects.all()
    return render(request, "books/list-books.html", {
        "books": books
    })


@user_passes_test(is_librarian, login_url="/")
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
        else:
            messages.error(request, "Foram encontrados erros no formulário.")
            return render(request, "books/book-form.html", {
                "form": BookForm(request.POST, request.FILES)
            })

    return render(request, "books/book-form.html", {
        "form": form
    })


@user_passes_test(is_librarian, login_url="/")
def addAuthor(request):
    form = AuthorForm()

    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)

        if form.is_valid():
            author = form.save(commit=False)
            author.first_name = author.first_name.title()
            author.last_name = author.last_name.title()
            author.save()
            messages.success(request, "Novo autor adicionado com sucesso.")
            return redirect("add-author")
        else:
            messages.error(request, "Foram encontrados erros no formulário.")
            return render(request, "books/author-form.html", {
                "form": AuthorForm(request.POST, request.FILES)
            })

    return render(request, "books/author-form.html", {
        "form": form
    })
