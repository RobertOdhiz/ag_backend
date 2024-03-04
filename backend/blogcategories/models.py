from django.db import models
from basemodel.models import BaseModel


class BlogCategory(BaseModel):
    """ """
    name = models.CharField(max_length=255, null=False)