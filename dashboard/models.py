from django.db import models


# Create your models here.
class Case(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)


class Evidence(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_url = models.CharField(max_length=255)
    file_extension = models.CharField(max_length=20)
    file_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
