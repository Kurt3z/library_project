from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
