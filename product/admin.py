from django.contrib import admin
from .models import Maxsulot

@admin.register(Maxsulot)
class MaxsulotAdmin(admin.ModelAdmin):
    list_display = ['hajmi']
