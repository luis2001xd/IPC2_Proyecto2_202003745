from Escritorios import lista_escritorios
class puntos:
    def __init__(self,id,nombre,direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.escritorios = lista_escritorios()


class nodo_puntos:
    def __init__(self, puntos: puntos, siguiente = None):
        self.puntos = puntos
        self.siguiente = siguiente


class lista_puntos:
    def __init__(self):
        self.primero = None


    def agregar(self,puntos : puntos):
        
        if self.primero == None:
            self.primero = nodo_puntos(puntos = puntos)

        else: 
            nodoaux = self.primero
            
            while nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente

            nuevo_nodo = nodo_puntos(puntos = puntos)
            nodoaux.siguiente = nuevo_nodo

