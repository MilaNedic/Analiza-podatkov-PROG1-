# Analiza-podatkov-PROG1
**Projektna naloga pri predmetu Programiranje 1**

Najbolj popularni animeji

Analizirala bom prvih 490 najbolj popularnih animejev animejev(ki so že bili predvajani/so zaključeni)
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
Datoteka zajem_podatkov.py je bila narejena za zajem podatkov in izdelavo csv datoteke s podatki (ki se nahaja v mapi anime).
Mapa anime vsebuje prvih 10 strani html datotek (torej zajema prvih 490 naslovov - na stran pride ravno 49 animejev), anime.csv pa vsebuje obdelane podatke, torej naslov, opis, oceno, tip animeja, število epizod, oceno, začetek in konec predvajanja, število glasov in maturity rating. 
(orodja.py je bila pomožna datoteka, ki pa je nisem uporabila)
Datoteke s končnico .json skrbijo za pravilno delovanje delovanje ostalih datotek. 
