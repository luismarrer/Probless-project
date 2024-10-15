from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_owner = models.BooleanField(default=False)
    dept = models.ForeignKey("workspace.Department", verbose_name=("department"), on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('user', 'User')], default='user')

    def __str__(self):
        return self.username

