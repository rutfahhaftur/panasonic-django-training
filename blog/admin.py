from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = 'body'

# admin.site.register (ตาราง,คลาส)
admin.site.register(Post, PostAdmin)