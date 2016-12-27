import orodja
import re
import requests
import time


def zajemi_podatke():
    for stran in range(1, 1500, 20):
        osnovni_naslov = 'http://www.androidrank.org/listcategory?category=&start='
        parametri = '&sort=4&price=all&hl=en'
        naslov = '{}{}{}'.format(osnovni_naslov, stran, parametri)
        ime_datoteke = 'aplikacijee/ aplikacije, {}.html'.format(stran)
        orodja.shrani(naslov, ime_datoteke)

def pripravi_aplikacije():
    regex_aplikacije = re.compile(
        r'<a href="/application/(?P<povezava>.+?)?hl=en">(?P<ime>.+?)</a>',
        flags=re.DOTALL
    )

    for html_datoteka in orodja.datoteke('aplikacije/'):
        for aplikacija in re.finditer(regex_aplikacije, orodja.vsebina_datoteke(html_datoteka)):
            naslovcek = '{}{}'.format('http://www.androidrank.org/application/', aplikacija.group('povezava'))
            imencek = 'app/{}.html'.format(aplikacija.group('ime'))
            orodja.shrani(naslovcek, imencek)

zajemi_podatke()
pripravi_aplikacije()
