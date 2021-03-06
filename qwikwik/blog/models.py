from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
   #about = models.CharField(max_length=200)
    text = models.TextField() 
    tags_Name_Of_Blog = models.CharField(max_length=200)
    tags_Place = models.CharField(max_length=200)
    tags_Season = models.CharField(max_length=200)
    url = models.URLField(max_length=255, blank=True)
    country = models.CharField(max_length=2, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipCode = models.CharField(max_length=7, blank=True, null=True)
    created_Date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
   # image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
   
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __self__(self):
        return self.title
