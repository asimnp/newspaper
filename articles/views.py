from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "articles/list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail.html"


class ArticleEditView(UpdateView):
    model = Article
    template_name = "articles/edit.html"
    fields = ("title", "body", "publish")


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = reverse_lazy("articles:list")
