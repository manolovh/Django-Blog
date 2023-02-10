from django.contrib import admin

from .models import Author, Post, Tag, Comment

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name',)
    list_filter = ("first_name",)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",)
        }
    list_display = ("title", "date", "author")
    list_filter = ("title", "author", "tags")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")
    list_filter = ("user_name", "post")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)