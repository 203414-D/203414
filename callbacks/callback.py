import threading
import requests

def get_service(response_json_data):
    print(response_json_data)
    
def get_error():
    print("error")

def get_service_02(response_json_data):
    print(response_json_data)
    
def get_error_02():
    print("error")

def request_data(url, success_callback, error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()
        pass


class Hilo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
         h1 = threading.Thread(target=request_data,  kwargs={
            'url':"https://pokeapi.co/api/v2/pokemon?offset=0&limit=1154",
            'success_callback':get_service,
            'error_callback':get_error,

         })
       
         h1.start()

         h2 = threading.Thread(target=request_data,  kwargs={
            'url':"https://api.chucknorris.io/jokes/random",
            'success_callback':get_service_02,
            'error_callback':get_error_02,

         })
       
         h2.start()
hilo = Hilo()
hilo.start()
hilo2 = Hilo()
hilo2.start()
