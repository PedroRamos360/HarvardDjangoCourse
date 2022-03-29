from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'timestamp')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'timestamp')

admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
admin.site.register(Follower)
