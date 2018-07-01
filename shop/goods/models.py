from django.db import models


# Create your models here.
class GoodItem(models.Model):
    """A model of a rock band."""
    name = models.CharField(max_length=200)