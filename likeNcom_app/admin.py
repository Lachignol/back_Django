from django.contrib import admin

# Register your models here.
from .models import Comment,Like


class CommentAdmin(admin.ModelAdmin):
     model = Comment
     field = "__all__"
admin.site.register(Comment,CommentAdmin)


class LikeAdmin(admin.ModelAdmin):
     model = Like
     field = "__all__"   
admin.site.register(Like,LikeAdmin)
