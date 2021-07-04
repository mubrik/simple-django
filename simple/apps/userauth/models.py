from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class TimeStampedModel(models.Model):
    """time stamped model for subclass"""

    # set field to now when obj is created
    created = models.DateTimeField(auto_now_add=True)
    # set field to now when obj is saved
    modified = models.DateTimeField(auto_now=True)


class User(TimeStampedModel, AbstractUser):
    """Base user model,
    Extends django base abstract user and a timestamped model (created, modified),
    id and pk is randomcharfield, 10 keys
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True,
    )
