from django.db import models
from users.models import NewUser
from ghalas.models import Ghala
from django.utils import timezone

class MyGhala(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    ghala = models.ManyToManyField(Ghala)
    bags_sold = models.IntegerField(default=0)
    date_rented = models.DateTimeField(default=timezone.now)
    duration_of_storage = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name
