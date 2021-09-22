import threading
import time
import random


class Minero:

    def __init__(self, nombre):
        self.nombre = nombre
        self.velocidad = random.randint(2, 4)
        self.cantidad = 0
        self.adentro = False

    def recolectar_recursos(self):
        cantidad = random.randint(5, 15)
        tiempo = cantidad/self.velocidad
        self.adentro = True
        time.sleep(tiempo)
        print(f'Trabajador {self.nombre} ha recolectado {cantidad} DCCriptoMonedas')
        self.cantidad += cantidad
        self.adentro = False

    def trabajar(self):
        for i in range(3):
            print(f'Trabajador {self.nombre} ha entrado a la DCCueva')
            self.recolectar_recursos()


t1 = Minero('John')
t2 = Minero('Alex')
t3 = Minero('Peter')
def empezar_trabajo(tn):
    tn.trabajar()
th1 = threading.Thread(target=empezar_trabajo,kwargs={"tn":t1})
th2 = threading.Thread(target=empezar_trabajo,kwargs={"tn":t2})
th3 = threading.Thread(target=empezar_trabajo,kwargs={"tn":t3})
th1.start()
th2.start()
th3.start()
th1.join()
th2.join()
th3.join()
total = t1.cantidad + t2.cantidad + t3.cantidad
print('------------------------------------------')
print(f'Se han recolectado {total} DCCriptoMonedas')
