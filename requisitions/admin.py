from django.contrib import admin

from .models.requisition import Requisition
from .models.tier import Tier

admin.site.register(Requisition)
admin.site.register(Tier)
