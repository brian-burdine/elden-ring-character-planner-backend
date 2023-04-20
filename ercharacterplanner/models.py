from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

## Data Models
## Grabbed from ERDB API (https://api.erdb.wiki/v1/latest/)

class Weapon (models.Model):
    name = models.CharField(max_length=75)
    category = models.ForeignKey('Weapon_Type', on_delete=models.PROTECT)
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    default_skill_id = models.IntegerField()
    allow_ash_of_war = models.BooleanField()
    upgrade_material = models.ForeignKey('Upgrade_Material', on_delete=models.PROTECT)
    attribute_requirement = models.ManyToManyField('Attribute_Requirement')

    def __str__(self):
        return self.name

class Weapon_Type (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Upgrade_Material (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name