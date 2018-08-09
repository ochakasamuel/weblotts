from django.contrib import admin
from .models import Page, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'category', 'slug')
    list_filter = ('page_title', 'slug')
    search_fields = ('page_title', 'page_content')
    prepopulated_fields = {'slug': ('page_title',)}


admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)

