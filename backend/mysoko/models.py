from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from users.models import NewUser
from myghala.models import MyGhala
from soko.models import Soko

class MySoko(models.Model):
    my_ghala = models.ForeignKey(MyGhala, on_delete=models.CASCADE)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    commodity_sold = models.ForeignKey(Soko, on_delete=models.CASCADE)
    bags_sold = models.IntegerField(default=0)
    date_sold = models.DateTimeField(default=timezone.now)


    def clean(self):
        # Check if the commodity_sold exists in the associated MyGhala
        if self.commodity_sold not in self.my_ghala.commodity_stored.all():
            raise ValidationError("The commodity sold is not in the MyGhala.")

        # Check if the user is the owner of the MyGhala
        if self.user != self.my_ghala.user:
            raise ValidationError("You can only sell from your own MyGhala.")
        
         # Check if bags_sold is greater than bags_stored
        if self.bags_sold > self.my_ghala.bags_stored:
            raise ValidationError("Bags sold cannot exceed bags stored in MyGhala.")

    def __str__(self):
        return f"Sold by {self.user.first_name}"

    def calculate_amount_received(self):
        return self.bags_sold * self.commodity_sold.price

    def update_bags_stored(self, bags_added):
        my_ghala_entry, created = MyGhala.objects.get_or_create(user=self.user, ghala=self.commodity_sold.ghala)
        my_ghala_entry.bags_stored += bags_added
        my_ghala_entry.save()