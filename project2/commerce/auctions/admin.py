from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class AuctionListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'user', 'category')

admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(AuctionList, AuctionListAdmin)
