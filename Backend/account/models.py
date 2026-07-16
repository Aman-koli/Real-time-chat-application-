from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True,
    )

    bio = models.TextField(
        blank=True
    )

    is_online = models.BooleanField(
        default=False
    )

    last_seen = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )