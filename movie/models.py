from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=200, unique=True)
    #title = display_title
    description = models.CharField(max_length=1000, default='description')
    #description= headline
    year=models.IntegerField(default='year')
    #year=opening_date
    summary=models.TextField(default='summary')
    #summary = summary_short
    image=models.TextField(default='image')
    #image = src
    def __str__(self):
        return self.title

    #maybe don't need this but:
    # def get_absolute_url(self):
    #     return reverse('movie_detail', kwargs={'pk':self.pk})