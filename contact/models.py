from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    mobil = models.IntegerField(max_length=10)


    class Meta:
        db_table = "information"

