import time
import random
from threading import Thread


# Implementar modelacion con Thread...
# ... puedes usar herencia si quieres ;)
class Minero(Thread):

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.velocidad = random.randint(2, 4)
        self.cantidad = 0
        self.adentro = False
        self.daemon = True
        pass

    def recolectar_recursos(self):
        cantidad = random.randint(5, 15)
        tiempo = cantidad/self.velocidad
        self.adentro = True
        time.sleep(tiempo)
        print(f'Trabajador {self.nombre} ha recolectado {cantidad} DCCriptoMonedas')
        self.cantidad += cantidad
        self.adentro = False

    def trabajar(self):
        self.start()
        
    def run(self): #Puedes modificarlo si quieres trabajar con herencia ;)
        for i in range(3):
            print(f'Trabajador {self.nombre} ha entrado a la DCCueva')
            self.recolectar_recursos()
        pass

class Demoledor:

    def __init__(self, trabajadores):
        self.trabajadores = trabajadores

    def demoler(self):
        print('La DCCueva ha sido derrumbada')
        chequeador = [trabajador.adentro for trabajador in self.trabajadores]
        if True in chequeador:
            cantidad = chequeador.count(True)
            if cantidad != 1:
                print(f'Que desastre, han muerto {cantidad} trabajadores')
            else:
                print(f'Que desastre, ha muerto {cantidad} trabajador')
        else:
            print('Buen trabajo, ningun trabajador salio herido') 

t1 = Minero('John') #Eres libre de modificar los nombres :)
t2 = Minero('Alex') #Eres libre de modificar los nombres :)
t3 = Minero('Peter') #Eres libre de modificar los nombres :)
demoledor = Demoledor([t1, t2, t3])

#Acá debes inciiar los threads
t1.trabajar()
t2.trabajar()
t3.trabajar()

#No modificar
time.sleep(5)
total = t1.cantidad + t2.cantidad + t3.cantidad
print('------------------------------------------')
print(f'Se han recolectado {total} DCCriptoMonedas')
t1.join()
t2.join()
t3.join()
demoledor.demoler()