from django.db import models
from users.models import NewUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from basemodel.models import BaseModel


class FarmerProfile(BaseModel):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(unique=True, null=True, max_length=13)
    address = models.CharField(default="", max_length=250)
    avatar = models.ImageField(upload_to='avatars/', default='default.jpg', null=True)

    def __str__(self):
        return self.user.first_name

@receiver(post_save, sender=NewUser)
def create_farmer_profile(sender, instance, created, **kwargs):
    if created:
        FarmerProfile.objects.create(user=instance)

@receiver(post_save, sender=NewUser)
def save_farmer_profile(sender, instance, **kwargs):
    instance.farmerprofile.save()
