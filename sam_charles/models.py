from django.db import models

# Create your models here.

class Song(models.Model):
    GENRES = (
        ('country', 'Country'),
        ('pop', 'Pop'),
        ('folk', 'Folk'),
    )
    
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=GENRES)
    url = models.URLField(default=None)
    
    def __str__(self):
        return f'Song: {self.title} | Genre: {self.genre}'