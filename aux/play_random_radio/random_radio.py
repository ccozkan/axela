import os
import json
from random import randint

with open('radio_stations.json') as json_file:
    radio_stations = json.load(json_file)

def play_random_radio():
    os.system('mpv ' + random(radio_stations))

def random(array):
    index = randint(0, len(array))
    return array[index]["url"]

def stop_radio():
    os.system('killall mpv')
