from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.ArticleEditView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.ArticleDeleteView.as_view(), name="delete"),
    path("", views.ArticleListView.as_view(), name="list"),
]
