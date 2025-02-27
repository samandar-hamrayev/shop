from django.contrib import admin

from .models import Product, Category, Comment


class ProductAdmin(admin.ModelAdmin):
    #admin panelda ko'rsatilagin maydonlar
    list_display = ('name', 'price', 'discount', 'category','rating', 'quantity', 'created_at', 'updated_at')

    #filterlashdagi maydonlar
    list_filter = ('category', 'rating', 'discount')

    #qidirganda qidiriluvchi maydonlar
    search_fields = ('name', 'discount')

    #tartiblash, narx bo'yicha kamayish
    ordering = ['-price']

    #qayta edit qilishda ko'rsatilagan maydonlar
    fields = ('name', 'description', 'price', 'discount', 'category', 'rating', 'quantity', 'image')

    #faqat korish mumkin bolgan maydonlar
    readonly_fields = ('discounted_price',)

    #batafsil objectga kirmasdan tahrirlash mumkin bo'lgan maydonlar
    list_editable = ('price', 'quantity',)




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')

    list_filter = ('created_at', 'updated_at')

    search_fields = ('title',)

    ordering = ('title',)

    fields = ('title',)

    list_editable = ('title',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
