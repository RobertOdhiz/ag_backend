from django.db import models

class Feedback(models.Model):
    email = models.EmailField()
    feedback_text = models.TextField()

    def __str__(self):
        return self.email
