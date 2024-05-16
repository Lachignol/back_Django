from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
     model = Comment
     field = "__all__"
admin.site.register(Comment,CommentAdmin)



