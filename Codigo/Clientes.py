from Transacciones import lista_transacciones

class clientes:
    def __init__(self,dpi,nombre):
        self.dpi = dpi
        self.nombre = nombre
        self.transacciones = lista_transacciones ()

class nodo_clientes:
    def __init__(self, cliente : clientes,siguiente = None):
        self.cliente = cliente
        self.siguiente = siguiente

class lista_clientes:
    def __init__(self):
        self.primero = None

    def agregar(self, cliente : clientes):

        if self.primero == None:
            self.primero = nodo_clientes(cliente = cliente)

        else: 
            nodoaux = self.primero

            while nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente

            nuevo_cliente = nodo_clientes (cliente = cliente)
            nodoaux.siguiente = nuevo_cliente


    def imprimir(self):
        nodoaux = self.primero

        while nodoaux != None:
            print("Cliente",nodoaux.cliente.nombre)
            print("Transacciones: ")
            nodoaux.cliente.transacciones.imprimir()
            nodoaux = nodoaux.siguiente

