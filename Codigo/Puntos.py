import imp
from Escritorios import lista_escritorios
from Clientes import lista_clientes
from Lista_activos import lista_activos
from Lista_desactivados import lista_desactivados
class puntos:
    def __init__(self,id,nombre,direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.escritorios = lista_escritorios()
        self.cliente = lista_clientes ()
        self.activos = lista_activos ()
        self.desactivados = lista_desactivados ()
        self.tiempo_min_atencion = 0
        self.tiempo_max_atencion = 0
        self.tiempo_prom_atencion = 0
        self.tiempo_min_espera = 0
        self.tiempo_max_espera = 0
        self.tiempo_prom_espera = 0
        self.tiempo_total = 0

        
    
    def minimo_atencion(self,tiempo):
        if self.tiempo_min_atencion == 0:
            self.tiempo_min_atencion = tiempo
        
        else:
            if self.tiempo_min_atencion > tiempo:
                self.tiempo_min_atencion = tiempo


    def maximo_atencion(self,tiempo):
        if self.tiempo_max_atencion == 0:
            self.tiempo_max_atencion = tiempo
        
        else:
            if tiempo > self.tiempo_max_atencion:
                self.tiempo_max_atencion = tiempo


    def total_tiempo(self,tiempo): 
        self.tiempo_total += tiempo

    def calcular_promedio(self, tiempo, cantidad ):
        if cantidad != 0:
            self.tiempo_prom_atencion = tiempo/cantidad
            

    def minimo_espera(self,tiempo):
        if self.tiempo_min_espera == 0:
            self.tiempo_min_espera = tiempo


    def maximo_espera(self, tiempo):
        self.tiempo_max_espera = tiempo

    
    def calcular_promedio_espera (self,tiempo, cantidad):
        if cantidad != 0:
            self.tiempo_prom_espera = tiempo / cantidad

    

    


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


    

    
    

    
    


    

