from django.db import models

# Create your models here.

class customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    phone      = models.IntegerField()
    view       = models.TextField()

    def __str__(self):
        return self.first_name