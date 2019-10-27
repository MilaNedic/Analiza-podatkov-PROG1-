import requests
import re
import os
import csv
import orodja

anime_na_stran = 50
skupno_stevilo = 250

#def filmi_na_strani(st_strani, na_stran=50):
#    url = (
#        f'https://myanimelist.net/anime.php?q=&type=0&score=0&status=2&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c[0]=a&c[1]=b&c[2]=c&c[3]=d&c[4]=e&c[5]=f&c[6]=g&gx=0&'
#        f'&show={(st_strani - 1) * na_stran + 1}'
#    )
#    ime_datoteke = 'zajeti-podatki/najbolj-znani-filmi-{}.html'.format(st_strani)
#    orodja.shrani_spletno_stran(url, ime_datoteke)
#    vsebina = orodja.vsebina_datoteke(ime_datoteke)

# definiratje URL glavne strani bolhe za oglase z mačkami
anime_frontpage_url = 'https://myanimelist.net/anime.php?q=&type=0&score=0&status=2&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c[0]=a&c[1]=b&c[2]=c&c[3]=d&c[4]=e&c[5]=f&c[6]=g&gx=0&show=0'
# mapa, v katero bomo shranili podatke
anime_directory = 'anime'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = 'index_anime.html'
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = 'anime.csv'

def download_url_to_string(url):
    """Funkcija kot argument sprejme niz in puskuša vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        # del kode, ki morda sproži napako
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

def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

# Definirajte funkcijo, ki prenese glavno stran in jo shrani v datoteko.


def save_frontpage(directory, filename):
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz"""
    text = download_url_to_string(cats_frontpage_url)
    save_string_to_file(text, directory, filename)
    return None