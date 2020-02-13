# Analiza-podatkov-PROG1
**Projektna naloga pri predmetu Programiranje 1**

**UVOD**

Analizirala bom prvih 1960 najbolj popularnih animejev animejev(ki so že bili predvajani/so zaključeni)
* [myanimelist](https://myanimelist.net/anime.php?q=&type=0&score=0&status=2&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B%5D=a&c%5B%5D=b&c%5B%5D=c&c%5B%5D=d&c%5B%5D=e&c%5B%5D=f&c%5B%5D=g&gx=0)

------------------------------------------------------------------------------

Za vsak anime bom zajela:
* naslov
* začetek in konec predvajanja
* žanr
* oceno in število glasov
* število epizod
* oceno vsebine (content/maturity rating)

Delovne hipoteze:
* Ali obstaja povezava med žanrom in popularnostjo (oceno)?
* Katera vsebina je najbolj gledana (G, PG, ...)?
* Ali število epizod vpliva na gledanost/oceno?

----------------------------------------------------------------------------

**O repozitoriju**

Datoteka zajem_podatkov.py je bila narejena za zajem podatkov s spletne strani in izdelavo csv datoteke s podatki o pozamenih animejih (ki se nahaja v mapi anime).

Mapa anime vsebuje prvih 40 strani html datotek (torej zajema prvih 1960 naslovov - na stran pride ravno 49 animejev), anime.csv pa vsebuje obdelane podatke, torej naslov, opis, oceno, tip animeja, število epizod, oceno, začetek in konec predvajanja, število glasov in maturity rating. 

Datoteke s končnico .json skrbijo za pravilno delovanje delovanje ostalih datotek. 

(orodja.py je bila pomožna datoteka, ki pa je nisem uporabila)

Analiza podatkov se nahaja v datoteki analiza podatkov.ipynb.

(opomba: zaradi bolj reprezentativne analize podatkov sem število podatkov spremenila iz 490 na 1960, torej prvih 40 strani in ne samo prvih 10)

--------------------------------------------------------------------------

**Ugotovitve**
* Ena izmed glavnih ugotovitev je ta, da niti žanr niti vsebina ne vplivata na popularnost. 
* Ljudje nasploh radi gledajo animeje in njihve preference so zelo raznolike.
* Izmed analiziranih animejev je TV daleč najbolj popularen tip.
* Iz analize maturity ranting-a ugotovimo, da so ciljna publika najstniki, stari okrog 15 let.
