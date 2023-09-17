from django.db import models
from users.models import NewUser
from ghalas.models import Ghala
from soko.models import Soko
# from mysoko.models import MySoko
from django.utils import timezone

class MyGhala(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    ghala = models.ManyToManyField(Ghala)
    commodity_stored = models.ManyToManyField(Soko, related_name='ghalas_stored')
    bags_stored = models.IntegerField(default=0)
    date_rented = models.DateTimeField(default=timezone.now)
    duration_of_storage = models.IntegerField(default=0)

    def __str__(self):
        renter = "Rented by {}".format(self.user.first_name)
        return renter
    
    '''''
    def subtract_bags_sold(self):
        # Iterate through commodities stored in this MyGhala
        for commodity in self.commodity_stored.all():
            # Get the total bags sold for this commodity in MySoko
            total_bags_sold = MySoko.objects.filter(my_ghala=self, commodity_sold=commodity).aggregate(total_bags_sold=models.Sum('bags_sold'))['total_bags_sold']

            if total_bags_sold:
                # Subtract the bags sold from bags_stored
                self.bags_stored -= total_bags_sold
                # Save the updated bags_stored value
                self.save()
                '''