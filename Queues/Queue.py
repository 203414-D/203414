
import threading
import random
import queue
import time

cola=queue.Queue(10)

def producer():
    while True:
        if  not cola.full():
            producto = random.randint(1, 10)
            cola.put(producto)
            print('Productor ha insertado el producto: '+str(producto))
            time.sleep(3)
        else:
            time.sleep(3)


def consumer():
    while True:
        if not cola.empty():
            producto = cola.get()
            print('Consumidor ha tomado el producto: '+str(producto))
            time.sleep(3)
        else:
            time.sleep(3)

if __name__ == '__main__':
    productor = threading.Thread(target=producer)
    consumidor = threading.Thread(target=consumer)

    productor.start()
    consumidor.start()


