from django.contrib import admin

# Register your models here.

from .models import Comment
from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    fields = ["user","content"]
    list_display = ["user","content","created_time"]

    #
    pass

admin.site.register(Comment,CommentAdmin)
