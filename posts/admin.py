from django.contrib import admin

from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'draft', 'image', 'content', 'timestamp', 'updated']
    list_display_links = ['title']
    list_filter = ['draft', 'updated', 'timestamp']
    list_editable = []
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)
