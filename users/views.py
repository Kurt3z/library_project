from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, ReaderForm


def loginUser(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Nome de utilizador não existente.")
            return render(request, "users/login-register.html", {
                "page": page
            })

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Sessão iniciada com sucesso.")
            return redirect("index")
        else:
            messages.error(
                request, "Nome de utilizador ou palavra-passe incorretos.")

    return render(request, "users/login-register.html", {
        "page": page
    })


def registerUser(request):
    form = CustomUserCreationForm()
    page = "register"

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "A sua conta foi criada!")
            return redirect("index")
        else:
            messages.error(request, "Ocorreu um erro durante o registo.")

    context = {
        "form": form,
        "page": page
    }
    return render(request, "users/login-register.html", context)


def logoutUser(request):
    logout(request)
    messages.info(request, "Sessão encerrada com sucesso.")
    return redirect("login")


@login_required(login_url="login")
def userAccount(request):
    if request.user.contact.is_librarian:
        profile = request.user.contact.librarian
    else:
        profile = request.user.contact.reader
        form = ReaderForm(instance=profile)

    if request.method == "POST":
        # Needs to also handle Librarian profiles which is not doing yet - TERNARY OPERATOR
        form = ReaderForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com successo.")
            return redirect("account")
        else:
            messages.error(request, "Existem erros de validação.")
            return render(request, "users/account.html", {
                "form": ReaderForm(request.POST, request.FILES, instance=profile)
            })

    context = {
        "profile": profile,
        "form": form
    }
    return render(request, "users/account.html", context)
