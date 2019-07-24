from django.db import models
from django.urls import reverse


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=250)
    source = models.URLField(max_length=250, blank=True)
    cover = models.URLField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} by {self.author}"

    def get_absolute_url(self):
        return reverse('quote_detail', args=f"{self.id}")

    class Meta:
        ordering = ("-created",)
