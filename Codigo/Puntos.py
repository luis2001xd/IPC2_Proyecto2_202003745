from Escritorios import lista_escritorios
from Clientes import lista_clientes
class puntos:
    def __init__(self,id,nombre,direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.escritorios = lista_escritorios()
        self.cliente = lista_clientes ()


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


    def imprimir(self):

        nodoaux = self.primero 

        x=1
        while nodoaux != None:

            print("\n")
            print("--------Punto No."+str(x)+"-------------")
            print ("ID del punto:",nodoaux.puntos.id,", Nombre del punto:",nodoaux.puntos.nombre,", Dirección del punto:",nodoaux.puntos.direccion)
            x+=1
            nodoaux = nodoaux.siguiente


    def buscar_punto(self, id):

        nodoaux = self.primero

        while nodoaux.puntos.id != id:

            if nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente
            else:
                print ("Punto no encontrado")
                return None

        return nodoaux

    
    


    

