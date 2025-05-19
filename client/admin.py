from django.contrib import admin
from .models import Haridor

@admin.register(Haridor)
class HaridorAdmin(admin.ModelAdmin):
    list_display = ['ism_familiya']

