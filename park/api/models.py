from django.db import models

class Park(models.Model):
    carno = models.CharField(max_length=20)
    slot = models.IntegerField(unique=True,primary_key=True)




    class Meta:
        db_table='lot'
