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