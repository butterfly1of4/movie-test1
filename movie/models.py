from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    display_title=models.CharField(max_length=200, unique=True)
    # critics_pick=models.IntegerField(default='none')
    byline = models.CharField(max_length=1000, default='byline', unique=True)
    opening_date = models.CharField(default='year', max_length=50)
    headline = models.CharField(default='headline', max_length=2000)
    summary_short=models.TextField(default='summary')
    url=models.CharField(default='default-url', max_length=1000)
    image=models.TextField(default='image')
    #image = src
    def __str__(self):
        return self.title

    #maybe don't need this but:
    # def get_absolute_url(self):
    #     return reverse('movie_detail', kwargs={'pk':self.pk})