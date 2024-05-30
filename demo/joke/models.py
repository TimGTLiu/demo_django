from django.db import models

# Create your models here.

class Joke(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=1000)
    def __str__(self):
        return self.title

