

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'stock','category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')