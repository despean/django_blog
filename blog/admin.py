from django.contrib import admin
from .models import Post , Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status', 'created', 'updated')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    radio_fields = {'status': admin.VERTICAL}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['title', 'status', 'publish']
    readonly_fields = ('created', 'updated')

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active', 'updated')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
    readonly_fields = ('created', 'updated')
admin.site.register(Comment, CommentAdmin)