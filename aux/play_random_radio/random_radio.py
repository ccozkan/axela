import os
import json
from random import randint

with open('aux/play_random_radio/radio_stations.json') as json_file:
    radio_stations = json.load(json_file)

def play_random_radio():
    try:
        stop_radio()
    finally:
        random_station = random_element_of_an_array(radio_stations)
        os.system('espeak "' +  random_station['name'] + '" && sleep 2 && mpv ' + random_station['url'])

def random_element_of_an_array(array):
    index = randint(0, len(array) - 1)
    return array[index]

def stop_radio():
    os.system('pidof mpv | xargs kill -9')
