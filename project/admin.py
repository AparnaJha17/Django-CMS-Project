from django.contrib import admin
from .models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ("assets/js/blog.js",)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Banner)
admin.site.register(Social)
admin.site.register(Story)
admin.site.register(News)