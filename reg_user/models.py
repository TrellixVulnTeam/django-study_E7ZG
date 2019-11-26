from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

class reg_user(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    owner = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email
