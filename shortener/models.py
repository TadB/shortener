from django.db import models


class Link(models.Model):
    short = models.CharField(max_length=400)
    full_url = models.URLField(max_length=800, unique=True)
