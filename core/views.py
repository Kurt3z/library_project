from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .forms import PublisherForm, GenreForm, CountryForm


def is_librarian(user):
    return user.is_authenticated and user.contact.is_librarian


def index(request):
    return render(request, "core/index.html")


@user_passes_test(is_librarian, login_url="/")
def addPublisher(request):
    form = PublisherForm()

    if request.method == "POST":
        form = PublisherForm(request.POST, request.FILES)

        if form.is_valid():
            publisher = form.save(commit=False)
            publisher.name = publisher.name.title()
            publisher.save()
            messages.success(request, "Nova Editora adicionada com sucesso.")
            return redirect("add-publisher")
        else:
            messages.error(request, "Existem erros de validação.")
            return render(request, "core/publisher-form.html", {
                "form": PublisherForm(request.POST, request.FILES)
            })

    return render(request, "core/publisher-form.html", {
        "form": form
    })


@user_passes_test(is_librarian, login_url="/")
def addGenre(request):
    form = GenreForm()

    if request.method == "POST":
        form = GenreForm(request.POST)

        if form.is_valid():
            genre = form.save(commit=False)
            genre.caption = genre.caption.title()
            genre.save()
            messages.success(request, "Nova Género adicionado com sucesso.")
            return redirect("add-genre")
        else:
            messages.error(request, "Existem erros de validação.")
            return render(request, "core/genre-form.html", {
                "form": GenreForm(request.POST)
            })

    return render(request, "core/genre-form.html", {
        "form": form
    })


@user_passes_test(is_librarian, login_url="/")
def addCountry(request):
    form = CountryForm()

    if request.method == "POST":
        form = CountryForm(request.POST)

        if form.is_valid():
            country = form.save(commit=False)
            country.name = country.name.title()
            country.code = country.code.upper()
            country.save()
            messages.success(request, "Novo País adicionado com successo.")
            return redirect("add-country")
        else:
            messages.error(request, "Existem erros de validação.")
            return render(request, "core/country-form.html", {
                "form": CountryForm(request.POST)
            })

    return render(request, "core/country-form.html", {
        "form": form
    })
