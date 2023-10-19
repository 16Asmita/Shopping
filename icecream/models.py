from django.db import models

# Create your models here.
class Icecream(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


    class Meta:
        db_table = "flavours"


class Contact(models.Model):
    name = models.CharField(max_length=30)
    mobil = models.IntegerField(max_length=10)


    class Meta:
        db_table = "contact_info"

