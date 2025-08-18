from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles/list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "articles/detail.html"


class ArticleEditView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "articles/edit.html"
    fields = ("title", "body", "publish")


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = reverse_lazy("articles:list")


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "articles/create.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
