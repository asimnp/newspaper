from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import Truncator, slugify
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles"
    )

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["-created"]),
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return f"{Truncator(self.title).chars(50,  truncate="...")}"

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
