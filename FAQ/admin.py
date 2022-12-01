from django.contrib import admin
from .models import Quession

# Register your models here.
@admin.register(Quession)

class QuessionsAdmin(admin.ModelAdmin):
    list_display =('name', 'email', 'publish')
    date_hierarchy = 'publish'
    ordering = ('publish', )
