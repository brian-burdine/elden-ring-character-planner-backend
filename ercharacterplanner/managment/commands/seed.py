import requests
from django.core.management.base import BaseCommand
from ...models import (
    Armament, 
    Armor, 
    Ash_Of_War, 
    Great_Rune, 
    Spell, 
    Talisman,
    Main_Attribute,
    Starting_Class,
    Starting_Class_Attribute
)

# This module defines a custom CLI command to grab information from a data API
#   and store it in the database. 

class Command(BaseCommand):
  def handle(self, *args, **options):
    pass

# API URL to get data from latest game version
BASE_URL = "https://api.erdb.wiki/v1/latest/"

# Armaments
def get_armaments():
    END_POINT = "armaments/"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    armaments = req.json()
    return armaments

def seed_armaments():
    armaments = get_armaments()
    for arm in armaments:
        a = Armament(
            name=arm,
            data=armaments[arm],
        )
        a.save()

# Armor
def get_armor():
    END_POINT = "armor/"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    armor = req.json()
    return armor

def seed_armor():
    armor_data = get_armor()
    for piece in armor_data:
        a = Armor(
            name=piece,
            data=armor_data[piece],
        )
        a.save()

# Ashes of War
def get_ashes_of_war():
    END_POINT = "ashes-of-war/"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    ashes_of_war = req.json()
    return ashes_of_war

def seed_ashes_of_war():
    ashes = get_ashes_of_war()
    for ash in ashes:
        a = Ash_Of_War(
            name=ash,
            data=ashes[ash],
        )
        a.save()

# Great Runes
def get_great_runes():
    END_POINT = "tools/?query=category:Great Rune"
    url = BASE_URL + END_POINT
    req = requests.get(url, headers={'Content-Type': 'application/json'})
    great_runes = req.json()
    return great_runes

def seed_great_runes():
    great_runes = get_great_runes()
    for rune in great_runes:
        g = Great_Rune(
            name=rune,
            data=great_runes[rune]
        )
        g.save()

# Spells
def get_spells():
    END_POINT = "spells/"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    spells = req.json()
    return spells

def seed_spells():
    spells = get_spells()
    for sp in spells:
        s = Spell(
            name=sp,
            data=spells[sp]
        )
        s.save()

# Talismans
def get_talismans():
    END_POINT = "talismans/"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    talismans = req.json()
    return talismans

def seed_talismans():
    talismans = get_talismans()
    for tali in talismans:
        t = Talisman(
            name=tali,
            data=talismans[tali]
        )

# Personally-defined Tables
# These are seed functions for tables that I didn't find a useful API to 
#   populate with. Modifications seem unlikely to Main_Attribute, 
#   Starting_Class, and Starting_Class_Attribute, but there probably will be
#   new Skills added in Shadow of the Erdtree. Hopefully I can find a useful
#   source for those

def seed_main_attributes():
    attributes = (
        "Vigor", "Mind", "Endurance", "Strength", "Dexterity", "Intelligence",
        "Faith", "Arcane"
    )
    for attribute in attributes:
        att = Main_Attribute(
            name=attribute
        )
        att.save()

def seed_starting_classes():
    starting_classes = (
        "Vagabond", "Warrior", "Hero", "Bandit", "Astrologer", "Prophet", 
        "Samurai", "Prisoner", "Confessor", "Wretch"
    )
    for start_class in starting_classes:
        sc = Starting_Class(
            name=start_class
        )
        sc.save()

def seed_starting_class_attributes():
    starting_class_attributes = {
        "Vagabond": {
            "Vigor": 15,
            "Mind": 10,
            "Endurance": 11,
            "Strength": 14,
            "Dexterity": 13,
            "Intelligence": 9,
            "Faith": 9,
            "Arcane": 7
        },
        "Warrior": {
            "Vigor": 11,
            "Mind": 12,
            "Endurance": 11,
            "Strength": 10,
            "Dexterity": 16,
            "Intelligence": 10,
            "Faith": 8,
            "Arcane": 9
        },
        "Hero": {
            "Vigor": 14,
            "Mind": 9,
            "Endurance": 12,
            "Strength": 16,
            "Dexterity": 9,
            "Intelligence": 7,
            "Faith": 8,
            "Arcane": 11
        },
        "Bandit": {
            "Vigor": 10,
            "Mind": 11,
            "Endurance": 10,
            "Strength": 9,
            "Dexterity": 13,
            "Intelligence": 9,
            "Faith": 8,
            "Arcane": 14
        },
        "Astrologer": {
            "Vigor": 9,
            "Mind": 15,
            "Endurance": 9,
            "Strength": 8,
            "Dexterity": 12,
            "Intelligence": 16,
            "Faith": 7,
            "Arcane": 9
        },
        "Prophet": {
            "Vigor": 10,
            "Mind": 14,
            "Endurance": 8,
            "Strength": 11,
            "Dexterity": 10,
            "Intelligence": 7,
            "Faith": 16,
            "Arcane": 10
        },
        "Samurai": {
            "Vigor": 12,
            "Mind": 11,
            "Endurance": 13,
            "Strength": 12,
            "Dexterity": 15,
            "Intelligence": 9,
            "Faith": 8,
            "Arcane": 8
        },
        "Prisoner": {
            "Vigor": 11,
            "Mind": 12,
            "Endurance": 11,
            "Strength": 11,
            "Dexterity": 14,
            "Intelligence": 14,
            "Faith": 6,
            "Arcane": 9
        },
        "Confessor": {
            "Vigor": 10,
            "Mind": 13,
            "Endurance": 10,
            "Strength": 12,
            "Dexterity": 12,
            "Intelligence": 9,
            "Faith": 14,
            "Arcane": 9
        },
        "Wretch": {
            "Vigor": 10,
            "Mind": 10,
            "Endurance": 10,
            "Strength": 10,
            "Dexterity": 10,
            "Intelligence": 10,
            "Faith": 10,
            "Arcane": 10
        }
    }

# # API Test
# great_runes = get_great_runes()
# gr_names = []
# for gr in great_runes:
#     print(gr)
#     gr_names.append(gr)
#     print(great_runes[gr]["summary"])