class escritorios:
    def __init__(self,id,identificacion,encargado):
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado

class nodo_escritorios:
    def __init__(self, escritorios : escritorios, siguiente = None):
        self.escritorios = escritorios
        self.siguiente = siguiente

class lista_escritorios:
    def __init__(self):
        self.primero = None

    def agregar(self, escritorio : escritorios):

        if self.primero == None:
            self.primero = nodo_escritorios(escritorios=escritorio)

        else: 
            nodoaux = self.primero

            while nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente

            nuevo_escritorio = nodo_escritorios (escritorios = escritorio)
            nodoaux.siguiente = nuevo_escritorio