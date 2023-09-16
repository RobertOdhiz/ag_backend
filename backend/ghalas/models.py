from django.db import models
from django.core.exceptions import ValidationError
from users.models import NewUser
from django.db.models import Avg

class Ghala(models.Model):
    ghala_name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    capacity = models.CharField(max_length=255)
    images = models.ImageField(upload_to="images/")
    start_price = models.IntegerField(default=0)
    rent_price = models.IntegerField(default=0)

    @property
    def average_rating(self):
        """
        Calculate and return the average rating for this Ghala.
        """
        ratings = Rating.objects.filter(ghala=self)
        avg_rating = ratings.aggregate(Avg('rating'))['rating__avg']
        return avg_rating or 0  # Return 0 if there are no ratings

    def __str__(self):
        return self.ghala_name

user = NewUser
ghala = Ghala

def validate_rating(value):
    """
    Validator for rating values.
    Ensures that the rating is within a sensible range, e.g., between 1 and 5.
    """
    if value < 1 or value > 5:
        raise ValidationError("Rating must be between 1 and 5.")

def validate_unique_rating(value):
    """
    Validator to ensure a user can rate a Ghala only once.
    """
    user_ratings = Rating.objects.filter(user=user, ghala=ghala)
    if user_ratings.exists():
        raise ValidationError("You have already rated this Ghala.")

# Usage in your Rating model:
class Rating(models.Model):
    ghala = models.ForeignKey(Ghala, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[validate_rating, validate_unique_rating])
