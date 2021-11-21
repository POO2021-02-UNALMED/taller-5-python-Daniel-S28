from zooAnimales import *
class Zona:
    def __init__(self,nombre=None,zoo=None):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=[]
    
    def agregarAnimales(self,animal):
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nom):
        self._nombre = nom
    
    def getAnimales(self):
        return self._animales
    def setAnimales(self, a):
        self._animales = a
    
    def getZoo(self):
        return self._zoo   
    def setZoo(self, z):
        self._zoo = z