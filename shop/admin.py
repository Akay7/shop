from django.contrib import admin
from .models import Product, Tag


class TagAdmin(admin.ModelAdmin):
    fields = [('name', 'slug')]
admin.site.register(Tag, TagAdmin)


class ProductAdmin(admin.ModelAdmin):
    ordering = ['title', 'price',]
    list_display = [
        'title', 'price', 'in_stock', 'show',
    ]

admin.site.register(Product, ProductAdmin)

