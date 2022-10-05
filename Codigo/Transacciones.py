class transacciones:
    def __init__(self, id, nombre, minutos, cantidad = None):
        self.id = id
        self.nombre = nombre
        self.minutos = minutos
        self.cantidad = cantidad
        self.tiempo_total = 0




class nodo_transacciones:
    def __init__(self,transacciones : transacciones, siguiente = None):
        self.transacciones = transacciones
        self.siguiente = siguiente


class lista_transacciones:
    def __init__(self):
        self.primero = None
        self.tiempo_total = 0

    def agregar(self, transaccion : transacciones):
        if self.primero == None:
            self.primero = nodo_transacciones(transacciones=transaccion)

        else:
            nodoaux = self.primero

            while nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente

            nueva_transaccion = nodo_transacciones(transacciones = transaccion)
            nodoaux.siguiente = nueva_transaccion

    def imprimir(self):
        nodoaux = self.primero
        print("--------Transacciones de la empresa--------")
        while nodoaux != None:
            print("Id de la transaccion:", nodoaux.transacciones.id, ", Nombre de la transaccion:",nodoaux.transacciones.nombre,", Tiempo de la transaccion: ",nodoaux.transacciones.minutos)
            nodoaux = nodoaux.siguiente

    def buscar_transaccion(self,id):
        nodoaux = self.primero

        while nodoaux.transacciones.id != id:

            if nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente
            
            else: 
                return None

        return nodoaux


    def calcular_tiempo(self):
        nodoaux = self.primero
        tiempo_transaccion = 0

        while nodoaux != None:
            tiempo_transaccion = nodoaux.transacciones.cantidad * nodoaux.transacciones.minutos
            self.tiempo_total+=tiempo_transaccion
            nodoaux = nodoaux.siguiente

        return self.tiempo_total

    def calcular(self):
        nodoaux = self.primero
        tiempo_transaccion = 0
        tiempo_total = 0

        while nodoaux != None:
            tiempo_transaccion = nodoaux.transacciones.cantidad * nodoaux.transacciones.minutos
            tiempo_total+=tiempo_transaccion
            nodoaux = nodoaux.siguiente

        return tiempo_total




