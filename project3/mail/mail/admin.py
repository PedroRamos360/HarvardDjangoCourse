from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'user', 'subject', 'timestamp')


admin.site.register(User, UserAdmin)
admin.site.register(Email, EmailAdmin)