from django.contrib import admin
from .models import Kitoblar
# Register your models here.

@admin.register(Kitoblar)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','nashr', 'year']
    list_filter = ['title', 'year']
    search_fields = ['title', 'nashr']
    