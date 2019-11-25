from django.contrib import admin
from .models import Comment
# Register your models here.

        #把models创建的模型进行注册
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']
 
 
admin.site.register(Comment, CommentAdmin)