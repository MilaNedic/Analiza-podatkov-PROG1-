import requests
import re
import os
import csv
import orodja
import time

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

stevilo_strani = 10
# mapa, v katero bomo shranili podatke
anime_directory = 'anime'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = '{}_anime.html'
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

    #text = str()
    
    
    #for i in range(stevilo_strani):
    for i in range(1):
        text = ""
        anime_frontpage_url = 'https://myanimelist.net/anime.php?q=&type=0&score=0&status=2&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c[0]=a&c[1]=b&c[2]=c&c[3]=d&c[4]=e&c[5]=f&c[6]=g&gx=0&show={}'
        print(i)
        anime_frontpage_url = anime_frontpage_url.format(i * 50)

        text = download_url_to_string(anime_frontpage_url)
        print("First try")
        
        j = 0
        while text == None and j < 20:
            print("     Trying again:", i)
            time.sleep(1)
            text = download_url_to_string(anime_frontpage_url)
            j += 1
        if j == 20:
            print("Prevec neuspelih poizkusov")

        save_string_to_file(text, directory, filename.format(i))
        

    
    return None

###############################################################################
# Po pridobitvi podatkov jih želimo obdelati.
###############################################################################


def read_file_to_string(directory, filename):
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz"""
    frontpage_filename = '{}_anime.html'
    filename = frontpage_filename.format(0)
    
    path = os.path.join(directory, filename)


    with open(path, 'r', encoding='utf-8') as file_in:
        return file_in.read()

# Definirajte funkcijo, ki sprejme niz, ki predstavlja vsebino spletne strani,
# in ga razdeli na dele, kjer vsak del predstavlja en oglas. To storite s
# pomočjo regularnih izrazov, ki označujejo začetek in konec posameznega
# oglasa. Funkcija naj vrne seznam nizov.


def page_to_ads(page_content):
    """Funkcija poišče posamezne animeje, ki se nahajajo v spletni strani in
    vrne njih seznam"""
    rx = re.compile(r'<a class="hoverinfo_trigger.*?>(.*?)<div class="picSurround">',
                    re.DOTALL)
    ads = re.findall(rx, page_content)
    return ads

# Definirajte funkcijo, ki sprejme niz, ki predstavlja oglas, in izlušči
# podatke o imenu, ceni in opisu v oglasu.


def get_dict_from_ad_block(block):
    """Funkcija iz niza za posamezen blok izlušči podatke o ??? ki vsebuje ustrezne podatke
    """
    rx = re.compile(r'title="(?P<name>.*?)"'
                    r'.*?</h3>\s*(?P<description>.*?)\s*</?div'
                    r'.*?class="price">(<span>)?(?P<price>.*?)'
                    r'( €</span>)?</div',
                    re.DOTALL)
    data = re.search(rx, block)
    ad_dict = data.groupdict()
    return ad_dict

# Definirajte funkcijo, ki sprejme ime in lokacijo datoteke, ki vsebuje
# besedilo spletne strani, in vrne seznam slovarjev, ki vsebujejo podatke o
# vseh oglasih strani.


def ads_from_file(filename, directory):
    """Funkcija prebere podatke v datoteki "directory"/"filename" in jih
   pretvori (razčleni) v pripadajoč seznam slovarjev za vsak oglas posebej."""
    page = read_file_to_string(filename, directory)
    blocks = page_to_ads(page)
    ads = [get_dict_from_ad_block(block) for block in blocks]
    return ads


def ads_frontpage():
    return ads_from_file(anime_directory, frontpage_filename)

###############################################################################
# Obdelane podatke želimo sedaj shraniti.
###############################################################################


def write_csv(fieldnames, rows, directory, filename):
    """
    Funkcija v csv datoteko podano s parametroma "directory"/"filename" zapiše
    vrednosti v parametru "rows" pripadajoče ključem podanim v "fieldnames"
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None

# Definirajte funkcijo, ki sprejme neprazen seznam slovarjev, ki predstavljajo
# podatke iz oglasa mačke, in zapiše vse podatke v csv datoteko. Imena za
# stolpce [fieldnames] pridobite iz slovarjev.


def write_cat_ads_to_csv(ads, directory, filename):
    """Funkcija vse podatke iz parametra "ads" zapiše v csv datoteko podano s
    parametroma "directory"/"filename". Funkcija predpostavi, da sa ključi vseh
    sloverjev parametra ads enaki in je seznam ads neprazen.
    """
    # Stavek assert preveri da zahteva velja
    # Če drži se program normalno izvaja, drugače pa sproži napako
    # Prednost je v tem, da ga lahko pod določenimi pogoji izklopimo v
    # produkcijskem okolju
    assert ads and (all(j.keys() == ads[0].keys() for j in ads))
    write_csv(ads[0].keys(), ads, directory, filename)


# Celoten program poženemo v glavni funkciji

def main(redownload=True, reparse=True):
    """Funkcija izvede celoten del pridobivanja podatkov"""

    # Najprej v lokalno datoteko shranimo glavno stran
    save_frontpage(anime_directory, frontpage_filename)

    # Iz lokalne (html) datoteke preberemo podatke
    ads = page_to_ads(read_file_to_string(anime_directory, frontpage_filename))
    # Podatke prebermo v lepšo obliko (seznam slovarjev)
    ads_nice = [get_dict_from_ad_block(ad) for ad in ads]
    # Podatke shranimo v csv datoteko
    write_cat_ads_to_csv(ads_nice, anime_directory, csv_filename)

    # Dodatno: S pomočjo parameteov funkcije main omogoči nadzor, ali se
    # celotna spletna stran ob vsakem zagon prense (četudi že obstaja)
    # in enako za pretvorbo


if __name__ == '__main__':
    main()

