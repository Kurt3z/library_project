from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
