from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("register/", views.registerUser, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("account/", views.userAccount, name="account"),
    path("staff/register/", views.registerLibrarian, name="register-librarian")

]
