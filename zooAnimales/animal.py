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
        from zooAnimales import Anfibio
        from zooAnimales import Ave
        from zooAnimales import Mamifero
        from zooAnimales import Pez
        from zooAnimales import Reptil
        return "Mamiferos : {}\nAves : {}\nReptiles : {}\nAnfibios : {}".format(Mamifero.cantidadMamiferos(), 
        Ave.cantidadAves(), Reptil.cantidadReptiles(), Pez.cantidadPeces(), Anfibio.cantidadAnfibios())
    
    def setZona(self, z):
        self._zona = z
    
    def __str__(self):
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
        
    