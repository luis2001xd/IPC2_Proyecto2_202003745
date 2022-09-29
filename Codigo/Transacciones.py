class transacciones:
    def __init__(self, id, nombre, minutos, cantidad = None):
        self.id = id
        self.nombre = nombre
        self.minutos = minutos
        self.cantidad = cantidad


class nodo_transacciones:
    def __init__(self,transacciones : transacciones, siguiente = None):
        self.transacciones = transacciones
        self.siguiente = siguiente


class lista_transacciones:
    def __init__(self):
        self.primero = None

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

        while nodoaux != None:
            print("Id de la transaccion:", nodoaux.transacciones.id, ", Nombre de la transaccion:",nodoaux.transacciones.nombre,", Tiempo de la transaccion: ",nodoaux.transacciones.minutos,nodoaux.transacciones.cantidad)
            nodoaux = nodoaux.siguiente

    def buscar_transaccion(self,id):
        nodoaux = self.primero

        while nodoaux.transacciones.id != id:

            if nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente
            
            else: 
                return None

        return nodoaux
