from threading import Thread
import threading 
import time, random
import queue

bodega = queue.Queue(maxsize=20)

class Productor(Thread):
    def __init__(self, array1):
        threading.Thread.__init__(self)
        self.array1 = array1

    def run(self):
        while True:
            if not bodega.full():
                array1 = random.randint(0, 20)
                bodega.put(array1)
                print("Se agrego un nuevo intem: " + str(array1))
                time.sleep(5)

class Consumidor(Thread):
    def __init__(self,array2):
         threading.Thread.__init__(self)
         self.array = array2
        

    def run(self):
        while True:
            if not bodega.empty():
                array2 = bodega.get()
                print('Consumidor ha tomado el producto: '+str(array2))
                time.sleep(5)

def main():
    array=[]
    hilo_productor = Productor(array)
    hilo_consumidor = Consumidor(array)

    hilo_productor.start()
    hilo_consumidor.start()

main()



