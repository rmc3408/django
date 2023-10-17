from django.contrib import admin
from .models import Tag, Author, Post, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tag')
    list_display = ('title', 'author', 'get_tags')
    prepopulated_fields = {'slug': ('title', )}

    def get_tags(self, obj):
        return " / ".join([t.caption for t in obj.tag.all()])


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
