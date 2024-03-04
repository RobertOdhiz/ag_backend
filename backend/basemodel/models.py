from django.db import models
from uuid import uuid4
from django.utils import timezone


class BaseModel(models.Model):
    """Defines the BaseModel class"""
    id = models.UUIDField(primary_key=True, editable=False, null=False, default=uuid4())
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(default=timezone.now, null=False)
            

    class Meta:
        """ """
        abstract = True

    # def save(cls, *args, **kwargs):
    #     cls.updated_at = timezone.now()
    #     super().save(*args, **kwargs)
