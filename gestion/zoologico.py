class Zoologico:
    _zonas=[]
    def __init__(self,nombre=None,ubicacion=None):
        self._nombre=nombre
        self._ubicacion=ubicacion
    
    def cantidadTotalAnimales(self):
        total=0
        for z in self._zonas:
            total+=z.cantidadAnimales()
        return total
    
    def agregarZonas(self,zona):
        self._zonas.append(zona)
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nom):
        self._nombre = nom
    
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ub):
        self._ubicacion = ub
    
    @classmethod
    def getZona(cls):
        return cls._zonas  
    @classmethod    
    def setZonas(cls, zona):
        cls._zonas = zona
    



        