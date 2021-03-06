from django.contrib.gis.db import models
from django.contrib.auth.models import User
# Create your models here.


class Center(models.Model):
    """This model holds recycling centers."""
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.PointField(srid=4326)
    glass = models.BooleanField(default=False)
    paper = models.BooleanField(default=False)
    aluminum = models.BooleanField(default=False)
    plastic = models.BooleanField(default=False)
    oil = models.BooleanField(default=False)
    rechargeBatteries = models.BooleanField(default=False)
    electronics = models.BooleanField(default=False)
    paint = models.BooleanField(default=False)
    tires = models.BooleanField(default=False)
    cookGrease = models.BooleanField(default=False)
    scrapMetal = models.BooleanField(default=False)

    def __str__(self):
        """This displays the model by name on the admin page."""
        return "{}".format(self.name)


class Stand(models.Model):
    """This model holds produce stands."""
    name = models.CharField("Owner: ", max_length=40)
    address = models.CharField("Address: ", max_length=200)
    geom = models.PointField(srid=4326)
    descript = models.CharField("Available Produce: ", max_length=200)

    def __str__(self):
        """This displays the model by name on the admin page."""
        return "{}".format(self.name)


class Produce(models.Model):
    """This model will hold produce information as it relates to Stands"""
    name = models.ForeignKey(Stand)
    vegg = models.BooleanField(default=False)
    fruit = models.BooleanField(default=False)
    craft = models.BooleanField(default=False)

