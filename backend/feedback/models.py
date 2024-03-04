from django.db import models
from basemodel.models import BaseModel


class FeedBack(BaseModel):
    email = models.EmailField(null=True)
    text = models.TextField(null=False)