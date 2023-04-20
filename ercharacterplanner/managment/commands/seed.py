import requests
from django.core.management.base import BaseCommand
from models import Armament, Armor, Ash_Of_War, Great_Rune, Spell, Talisman

# This module defines a custom CLI command to grab information from a data API
#   and store it in the database. 

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

# # API Test
# great_runes = get_great_runes()
# gr_names = []
# for gr in great_runes:
#     print(gr)
#     gr_names.append(gr)
#     print(great_runes[gr]["summary"])