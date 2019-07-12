from django.db import models

BUS_NEEDED = [(1, ("Yes")),
  (2, ("No"))]

# Create your models here.
class Student(models.Model):
    std_id = models.PositiveIntegerField(unique=True, primary_key=True)
    std_name = models.CharField(max_length=255)
    Bus_needed = models.CharField(max_length=10,
                                       choices=BUS_NEEDED,default='')

