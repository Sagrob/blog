from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Author(AbstractUser):
    name = models.CharField(max_length=50)

    groups = models.ManyToManyField(Group, related_name='author_set')
    user_permissions = models.ManyToManyField(Permission, related_name='author_permissions')
    class Meta:
        db_table = "authors"