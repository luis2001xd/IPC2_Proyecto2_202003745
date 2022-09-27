class transacciones:
    def __init__(self, id, cantidad):
        self.id = id
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