from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publish", "created"]
    list_filter = ["author", "publish", "created"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "body"]
    raw_id_fields = [
        "author",
    ]
    show_facets = admin.ShowFacets.ALWAYS
    inlines = [CommentInline]
