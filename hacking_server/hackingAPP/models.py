from django.db import models

class Hacking_data(models.Model):
    source = models.CharField(max_length=200)
    data = models.CharField(max_length=200)

    def __str__(self):
        return self.source
