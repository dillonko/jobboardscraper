from django.db import models
from django.core.urlresolvers import reverse


class Organization(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse("organization_detail", args=[str(self.slug)])
