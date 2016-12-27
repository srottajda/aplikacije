import re
import orodja

regex_aplikacije = re.compile(
        r'<small>by <a href=.*?</a><br>\n        (?P<prenosi>.+?)\+ installs</small>.*?'
        r'<tr><th>Title:</th><td>(?P<ime>.+?)</td></tr>.*?'
        r'<tr><th>Developer:</th><td><a itemprop="author" href=".*?;hl=en">(?P<proizvajalec>.+?)</a></td></tr>.*?'
        r'<tr><th>Category:</th><td><a href=".*?;hl=en" itemprop="applicationCategory">(?P<kategorija>.+?)</a></td></tr>.*?'
        r'<tr><th>Price:</th><td>(?P<cena>.+?)</td></tr>.*?'
        r'<tr><th>Total ratings:</th><td itemprop="ratingCount">(?P<stevilo_ocen>.+?)</td></tr>.*?'
        r'<tr><th>Average rating:</th><td itemprop="ratingValue">(?P<ocena>.+?)</td></tr>.*?'
        ,
        flags=re.DOTALL
    )


def pocisti_aplikacijo(aplikacija):
    podatki = aplikacija.groupdict()
    podatki['ocena'] = float(podatki['ocena'])
    podatki['prenosi'] = int(podatki['prenosi'].replace(',',''))
    podatki['stevilo_ocen'] = int(podatki['stevilo_ocen'].replace(',',''))
    return podatki


def izloci_podatke_aplikacij(imenik):
    aplikacije = []
    for html_datoteka in orodja.datoteke(imenik):
        for aplikacija in re.finditer(regex_aplikacije, orodja.vsebina_datoteke(html_datoteka)):
            aplikacije.append(pocisti_aplikacijo(aplikacija))
    return aplikacije


aplikacije = izloci_podatke_aplikacij('app/')
orodja.zapisi_tabelo(aplikacije, ['ime', 'proizvajalec', 'kategorija', 'cena', 'stevilo_ocen', 'ocena', 'prenosi'], 'aplikacije.csv')
