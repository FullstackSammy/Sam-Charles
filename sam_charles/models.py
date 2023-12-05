from django.db import models

# Create your models here.

class Song(models.Model):
    GENRES = (
        ('country', 'Country'),
        ('pop', 'Pop'),
        ('folk', 'Folk'),
    )
    
    title = models.CharField(max_length=100)
    url = models.URLField(default=None)
    img = models.ImageField(upload_to=None, blank=True, null=True)
    genre = models.CharField(max_length=50, choices=GENRES)
    
    def __str__(self):
        return f'Song: {self.title} | Genre: {self.genre}'