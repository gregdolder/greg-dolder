from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    shortDescription = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name