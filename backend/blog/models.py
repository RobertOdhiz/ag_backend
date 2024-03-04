from django.db import models
from users.models import NewUser
from django.utils import timezone
from basemodel.models import BaseModel
from blogcategories.models import BlogCategory

class Blog(BaseModel):
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, blank=True)
    content = models.TextField()
    reads = models.IntegerField(default=0)
    image = models.ImageField(upload_to="blog/images/", default='blogdefault.jpg', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.author.first_name}'s blog"
    
    def increment_reads(self):
        self.reads += 1
        self.save()