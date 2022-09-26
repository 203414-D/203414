
import requests

def verificar(sitio):
    response = requests.head(sitio)
    if response.status_code == 200:
        response = requests.head(sitio)
        if response.status_code == 200:
            print(f'El sitio {sitio} esta activo')
        else:
            print(f'El sitio {sitio} no esta activo')
    else:
        print(f'El sitio {sitio} no esta activo')

if __name__=="__main__":
     sitio = ['https://matrixcalc.org/es/slu.htmll', 'https://www.google.com', 'https://www.facebook.com', 'https://animefenx.com/', 
        'https://www.amazon.com', 'https://www.wikipedia.org', 'https://wwww.reddit.com', 'https://www.twitter.com', 
        'https://www.instagram.com', 'https://www4.cuevana.pro/', 'https://www.tumblr.com', 'https://inmanga.com/', 
        'https://ww.netflix.com', 'https://www.ebay.com', 'https://wiki.supercombo.gg/w/Main_Page', 'https://www.imgur.com', 
        'https://www.craigsliaswst.org', 'https://snk.fandom.com/wiki/Main_Page', 'https://www.stackoverflow.com', 'https://www.apple.com', 
        'https://code.visualstudio.com/', 'https://www.office.com', 'https://www.fightergeneration.com/', 'https://www.chase.com', 
        'https://www.fightcade.com/']

for x in sitio:
 verificar(x)
