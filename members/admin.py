from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('staff', 'phone', 'address')
    list_filter = ('staff',)
    search_fields = ('birth_date', 'staff')
