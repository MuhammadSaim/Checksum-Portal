from django.db import models


# Create your models here.
class Case(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)