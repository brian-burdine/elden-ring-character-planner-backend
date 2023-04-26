from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Character (models.Model):
    name = models.CharField(max_length=16)
    starting_class = models.ForeignKey("Starting_Class", on_delete=models.CASCADE, blank=False, default=1)
    leveled_attributes = models.ManyToManyField("Main_Attribute", through="Character_Attribute")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Character_Attribute (models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attribute = models.ForeignKey("Main_Attribute", on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['character', 'attribute'],
                name='character_attribute_unique',
            ),
        ]

# DATA MODELS
#1. Grabbed from ERDB API (https://api.erdb.wiki/v1/latest/)

class Armament (models.Model):
    name = models.CharField(max_length=75)
    data = models.JSONField()

    def __str__(self):
        return self.name

class Armor (models.Model):
    name = models.CharField(max_length=100)
    data = models.JSONField()

    class Meta:
        verbose_name_plural = "armor"

    def __str__(self):
        return self.name

class Ash_Of_War (models.Model):
    name = models.CharField(max_length=75)
    data = models.JSONField()

    class Meta:
        verbose_name_plural = "ashes of war"

    def __str__(self):
        return self.name

class Great_Rune (models.Model):
    name = models.CharField(max_length=100)
    data = models.JSONField()

    def __str__(self):
        return self.name

class Spell (models.Model):
    name = models.CharField(max_length=100)
    data = models.JSONField()

    def __str__(self):
        return self.name

class Talisman (models.Model):
    name = models.CharField(max_length=100)
    data = models.JSONField()

    def __str__(self):
        return self.name

#2. Self-defined

class Main_Attribute (models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Starting_Class (models.Model):
    name = models.CharField(max_length=20)
    attributes = models.ManyToManyField(Main_Attribute, through='Starting_Class_Attribute')

    def __str__(self):
        return self.name

class Starting_Class_Attribute (models.Model):
    starting_class = models.ForeignKey(Starting_Class, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Main_Attribute(), on_delete=models.CASCADE)
    base_value = models.IntegerField()

# class Weapon (models.Model):
#     name = models.CharField(max_length=75)
#     category = models.ForeignKey('Weapon_Type', on_delete=models.PROTECT)
#     weight = models.DecimalField(max_digits=5, decimal_places=1)
#     default_skill_id = models.IntegerField()
#     allow_ash_of_war = models.BooleanField()
#     upgrade_material = models.ForeignKey('Upgrade_Material', on_delete=models.PROTECT)
#     attribute_requirement = models.ManyToManyField('Attribute_Requirement')

#     def __str__(self):
#         return self.name

# class Weapon_Type (models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

# class Upgrade_Material (models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name