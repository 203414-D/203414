import threading
import time
total_comidas_por_persona = [0]

palillo = threading.Lock()
def espera(numero):
    print("la persona " + str(numero) + " está esperando")
    time.sleep(1.25)
def comiendo(numero,indi):
    if(total_comidas_por_persona[indi-1] == 1):
        print("La persona " + str(numero) + " ya ha comido. Por lo que ya no lo hara más.")
    else:
     print("La perona " + str(numero) + " se prepara para comer")
    total_comidas_por_persona[indi-1] += 1
    tomar_palillos(numero)
    print("la persona " + str(numero) + " está comiendo")
    total_comidas_por_persona[indi-1] += 1
    time.sleep(1.25)
    dejar_palillos(numero)
def tomar_palillos(numero):
    try:
        palillo.acquire()
        print("La persona " + str(numero) + " tomó los palillos a su izquierda y derecha")
    except:
        print("Existió un problema al momento de usar los palillos")
def dejar_palillos(numero):
    try:
      print("la persona " + str(numero) + " terminó de comer y suelta los palillos")
      palillo.release()
    except:
        print("Existió un problema al momento de soltar los palillos")

def persona(numero, indi):
    while(total_comidas_por_persona[indi-1] <1):
        espera(numero)
        comiendo(numero, indi)

def main(id):
    j=1
    while id <=8:
        persona(id,j) 
        time.sleep(1.25)
        id +=1
    


class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id


    def run(self):
        main(self.id)

Hilos = [Hilo(1), Hilo(2), Hilo(3), Hilo(4), Hilo(5), Hilo(6),Hilo(7),Hilo(8)]
for h in Hilos:
    h.start()
