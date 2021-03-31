from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=200, )
    description = models.CharField(max_length=1000, default='description')
    year=models.IntegerField(default='year')
    summary=models.TextField()
    
    def __str__(self):
        return self.title