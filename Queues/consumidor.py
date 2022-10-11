import threading
import time
import queue
import random

class Bodega(threading.Thread):
    cola=queue.Queue(10)
    conta=0
    def __init__(self):
        super(Bodega, self).__init__()
        self.id = Bodega.conta
        Bodega.conta +=1
        Bodega.cola.put(threading.Lock())

    def producir():
        while True:
            if not Bodega.cola.full():
                producto = random.randint(1, 10)
                Bodega.cola.put(producto)
                print('Productor ha insertado el producto: '+str(producto))
                time.sleep(3)
            else:
                time.sleep(3)

    def consumir():
        while True:
            if not Bodega.cola.empty():
                producto = Bodega.cola.get()
                print('Consumidor ha tomado el producto: '+str(producto))
                time.sleep(3)
            else:
                time.sleep(3)

if __name__ == '__main__':
        productor = threading.Thread(target=Bodega.producir)
        consumidor = threading.Thread(target=Bodega.consumir)

        productor.start()
        consumidor.start()

