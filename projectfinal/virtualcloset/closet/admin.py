from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(ClothingCategory)
admin.site.register(LookCategory)
admin.site.register(ClothingItem)
admin.site.register(Look)

