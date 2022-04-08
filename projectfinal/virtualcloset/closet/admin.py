from django.contrib import admin

from .models import *

class ClothingCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name')

class ClothingItemyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'category')


admin.site.register(User)
admin.site.register(ClothingCategory, ClothingCategoryAdmin)
admin.site.register(LookCategory)
admin.site.register(ClothingItem, ClothingItemyAdmin)
admin.site.register(Look)

