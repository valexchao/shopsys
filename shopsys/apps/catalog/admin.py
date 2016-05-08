from django.contrib import admin
from .models import *
from .forms import ProductAdminForm
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ['name', 'price', 'old_price', 'created_at', 'updated_at']
    list_display_links = ['name']
    list_per_page = 30
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    list_display_links = ['name']
    list_per_page = 30
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}
