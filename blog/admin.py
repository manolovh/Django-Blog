from django.contrib import admin

from .models import Author, Post, Tag

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

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)