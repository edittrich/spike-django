from django.contrib import admin

from .models import BlogProject, BlogPost

admin.site.register(BlogProject)
admin.site.register(BlogPost)
