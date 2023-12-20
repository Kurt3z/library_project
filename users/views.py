from django.shortcuts import render


def loginUser(request):
    page = "login"
    context = {
        "page": page
    }
    return render(request, "users/login-register.html", context)


def registerUser(request):
    page = "register"
    context = {
        "page": page
    }
    return render(request, "users/login-register.html", context)
