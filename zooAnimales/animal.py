from gestion.zona import Zona

class Animal:
    _totalAnimales=0

    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._totalAnimales+=1
        self._zona=None
    
    @classmethod
    def totalPorTipo(self):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return "Mamiferos : {}\n Aves : {}\n Reptiles : {}\n Anfibios : {}".format(Mamifero.cantidadMamiferos(), 
        Ave.cantidadAves(), Reptil.cantidadReptiles(), Pez.cantidadPeces(), Anfibio.cantidadAnfibios())
    
    def setZona(self, z):
        self._zona = z
    
    def toString(self):
        if self._zona!=None:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + str(self._genero) + ", la zona en la que me ubico es " + str(self._zona) + ", en el " + str(self._zona.getZoo())
        return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + str(self._genero)

    def getNombre(self):
        return self._nombre
    def setNombre(self, nom):
        self._nombre = nom
    
    def getHabitat(self):
        return self._habitat
    def setHabitat(self, h):
        self._habitat = h
    
    def getGenero(self):
        return self._genero
    def setGenero(self, gen):
        self._genero = gen
    
    def getEdad(self):
        return self._edad
    def setEdad(self, ed):
        self._edad = ed
    
    def getZona(self):
        return self._zona
        
    