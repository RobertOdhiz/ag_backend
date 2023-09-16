from django.db import models
from ghalas.models import Ghala
from users.models import NewUser

class Soko(models.Model):
    commodity = models.CharField(max_length=255, blank=False)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/")
    ghala = models.ForeignKey(Ghala, on_delete=models.CASCADE)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.commodity
