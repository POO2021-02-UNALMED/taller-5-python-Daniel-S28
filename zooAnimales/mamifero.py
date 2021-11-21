from zooAnimales.animal import Animal
class Mamifero(Animal):
    caballos=0
    leones=0
    _listado=[]

    def __init__ (self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        self._listado.append(self)
    
    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        cls.caballos+=1
        return Mamifero(nombre,edad,"pradera",genero,True,4)
    
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        cls.leones+=1
        return Mamifero(nombre,edad,"selva",genero,True,4)
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls, lis):
        cls._listado = lis
        
    def isPelaje(self):
        return self._pelaje
    def setPelaje(self,p):
        self._pejale = p
            
    def getPatas(self):
        return self._patas
    def setPatas(self,pat):
        self._patas = pat
    


