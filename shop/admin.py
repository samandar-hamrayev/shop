from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Category, Comment, Order
from adminsortable2.admin import SortableAdminMixin
from import_export import resources
from import_export.admin import ImportExportMixin, ImportExportModelAdmin
from django.contrib import admin


#import export uchun resource modelllar
class ProductResuorces(resources.ModelResource):
    class Mete:
        model = Product

class CategoryResuorces(resources.ModelResource):
    class Mete:
        model = Category

class CommentResuorces(resources.ModelResource):
    class Mete:
        model = Comment

class OrderResuorces(resources.ModelResource):
    class Mete:
        model = Order


#tabular inline uchun modellar
class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class OrderInline(admin.TabularInline):
    model = Order
    extra = 1


    



class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #admin panelda ko'rsatiladigan maydonlar
    list_display = ('name', 'display_image', 'price', 'discount', 'category', 'rating', 'quantity', 'created_at', 'updated_at')

    #filterlashdagi maydonlar
    list_filter = ('category', 'rating', 'discount')

    #qidirganda qidiriluvchi maydonlar
    search_fields = ('name', 'discount')

    #tartiblash, narx bo'yicha kamayish
    ordering = ['my_order']

    #product qoshishda comment va order ham qosha oladi, garchi noreal bo'lsa ham
    inlines = [CommentInline, OrderInline]

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.image.url
            )
        return "Rasm yo‘q"

    display_image.short_description = "Rasm"




class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')

    list_filter = ('created_at', 'updated_at')

    search_fields = ('title',)

    ordering = ('title',)

    fields = ('title',)

    list_editable = ('title',)

    inlines = [ProductInline]

class CommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'created_at')

    list_filter = ('name', 'email', 'product')

    search_fields = ('name',)

    ordering = ('name',)

class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'phone', 'product', 'quantity', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('name', 'phone')
    ordering = ('-created_at',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Order, OrderAdmin)
