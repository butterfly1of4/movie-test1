from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000, default='description')
    year=models.IntegerField(default='year')
    summary=models.TextField()
    
    def __str__(self):
        return self.title
    
    #maybe don't need this but:
    # def get_absolute_url(self):
    #     return reverse('movie_detail', kwargs={'pk':self.pk})