from django.db import models

class Park(models.Model):
    plate = models.CharField(max_length=20)


def __str__(self):
    return self.plate
