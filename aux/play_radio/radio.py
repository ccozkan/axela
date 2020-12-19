import os
import json
from random import randint
from word2number import w2n

with open('aux/play_radio/radio_stations.json') as json_file:
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

def play_radio(index_word):
    index = w2n.word_to_num(index_word)
    radio_station = radio_stations[index]
    try:
        stop_radio()
    finally:
        os.system('espeak "' +  radio_station['name'] + '" && sleep 2 && mpv ' + radio_station['url'])

def list_radios():
    radio_list = ''
    for rs in range(0, len(radio_stations) - 1):
        radio_list = radio_list + 'radio #' + str(rs) + ' ' + radio_stations[rs]['name'] + "\n"
    return radio_list

