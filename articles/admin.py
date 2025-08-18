from django.contrib import admin

from .models import Article


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ["title", "author", "publish", "created"]
    list_filter = ["author", "publish", "created"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "body"]
    raw_id_fields = [
        "author",
    ]
    show_facets = admin.ShowFacets.ALWAYS
