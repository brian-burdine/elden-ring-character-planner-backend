import requests
from django.core.management.base import BaseCommand
from models import Armament, Armor, Ash_Of_War, Great_Rune, Spell, Talisman

# This module defines a custom CLI command to grab information from a data API
#   and store it in the database. 


BASE_URL = "https://api.erdb.wiki/v1/latest/"

def get_armaments():
    END_POINT = "armaments/"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    armaments = req.json()
    return armaments


def get_armor():
    END_POINT = "armor/"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    armor = req.json()
    return armor


def get_ashes_of_war():
    END_POINT = "ashes-of-war/"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    ashes_of_war = req.json()
    return ashes_of_war


def get_great_runes():
    END_POINT = "tools/?query=catgory:Great Rune"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    great_runes = req.json()
    return great_runes


def get_spells():
    END_POINT = "spells/"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    spells = req.json()
    return spells


def get_talismans():
    END_POINT = "talismans/"
    req = requests.get(BASE_URL + END_POINT, headers={'Content-Type': 
        'application/json'})
    talismans = req.json()
    return talismans
