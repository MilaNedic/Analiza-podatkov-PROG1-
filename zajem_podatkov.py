import requests
import re
import os
import csv

anime_na_stran = 50
skupno_stevilo = 250

#definiramo URL glavne strani z animeji 
anime_frontpage_url = '''https://myanimelist.net/anime.php?q=&type=0&
score=0&status=2&p=0&r=0&sm=0&sd=0&
sy=0&em=0&ed=0&ey=0&c%5B%5D=a&c%5B%5D=b&c%5B%5D=c&c%5B%
5D=d&c%5B%5D=e&c%5B%5D=f&c%5B%5D=g&gx=0'''

#mapa, v katero bomo shranili podatke
anime_directory = 'anime'

#ime datoteke, v katero bomo shranili strani s podatki
page_filename = 'anime.html'

#ime CSV datoteke, v katero bomo shranili podatke
csv_filename = 'anime.csv'

def download_url_to_string(url):
    '''Funkcije kot argument sprejme niz,
    skuša vrniti vsebino te speltne strani kot niz.
    Če pride do napake, naj vrne None'''
    try:
        #del kode, ki mora sprožiti napako
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        print("Napaka pri povezovanju do:", url)
        return None
    # nadaljujemo s kodo če ni prišlo do napake
    if r.status_code == requests.codes.ok:
        return r.text
    else:
        print("Napaka pri prenosu strani:", url)
        return None