from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import *


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff'),
        }),
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Librarian)
admin.site.register(Reader)
