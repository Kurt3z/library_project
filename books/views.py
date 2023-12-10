from django.shortcuts import render
from django.http import HttpResponse


def list_books(request):
    return HttpResponse("List all Library Books")
