
from concurrent.futures import thread
from tabnanny import check
import requests
from threading import Thread
import time

sitio = ['https://matrixcalc.org/es/slu.htmll', 'https://www.google.com', 'https://www.facebook.com', 'https://animefenx.com/', 
        'https://www.amazon.com', 'https://www.wikipedia.org', 'https://wwww.reddit.com', 'https://www.twitter.com', 
        'https://www.instagram.com', 'https://www4.cuevana.pro/', 'https://www.tumblr.com', 'https://inmanga.com/', 
        'https://ww.netflix.com', 'https://www.ebay.com', 'https://wiki.supercombo.gg/w/Main_Page', 'https://www.imgur.com', 
        'https://www.craigsliaswst.org', 'https://snk.fandom.com/wiki/Main_Page', 'https://www.stackoverflow.com', 'https://www.apple.com', 
        'https://code.visualstudio.com/', 'https://www.office.com', 'https://www.fightergeneration.com/', 'https://www.chase.com', 
        'https://www.fightcade.com/']


def verificar(sitio):
    response = requests.head(sitio)
    if response.status_code == 200:
        time.sleep(240)
        response = requests.head(sitio)
        if response.status_code == 200:
            print(f'El sitio {sitio} esta activo')
        else:
            print(f'El sitio {sitio} no esta activo')
    else:
        print(f'El sitio {sitio} no esta activo')


class Hilo(Thread):
    def __init__(self,sitio):
        Thread.__init__(self)
        self.sitio=sitio

    def run(self):
        verificar(self.sitio)

t1=[Hilo(sitio[0]), Hilo(sitio[1]), Hilo(sitio[2]), Hilo(sitio[3]), Hilo(sitio[4]), Hilo(sitio[5]), Hilo(sitio[6]), Hilo(sitio[7]), Hilo(sitio[8]), 
        Hilo(sitio[9]), Hilo(sitio[10]), Hilo(sitio[11]), Hilo(sitio[12]), Hilo(sitio[13]), Hilo(sitio[14]), Hilo(sitio[15]), Hilo(sitio[16]), Hilo(sitio[17]), 
        Hilo(sitio[18]), Hilo(sitio[19]), Hilo(sitio[20]), Hilo(sitio[21]), Hilo(sitio[22]), Hilo(sitio[23]), Hilo(sitio[24])]



for th in t1:
    th.start()


