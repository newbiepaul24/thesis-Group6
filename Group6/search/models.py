from django.db import models

# Create your models here.


class Name(models.Model):
    First = models.CharField(max_length=255)
    Last = models.CharField(max_length=255)
    YearDate = models.CharField(max_length=10)
    GraveKeeper = models.BooleanField(default=True)

