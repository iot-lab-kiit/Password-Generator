from django.db import models
from django.contrib.auth.models import User
from django.forms import widgets


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    previous_passwords = models.JSONField(default = {"passwords": []})


    def __str__(self):
        return self.user.first_name