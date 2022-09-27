from Puntos import lista_puntos
class empresa:
    def __init__(self,id,nombre,abreviatura):
        self.nombre = nombre
        self.id = id
        self.abreviatura = abreviatura
        self.puntos_atencion = lista_puntos()



class nodo_empresa:
    def __init__(self,empresa: empresa,siguiente = None):
        self.empresa = empresa
        self.siguiente = siguiente



class lista_empresa:

    def __init__(self):
        self.primero = None


    def agregar(self,empresa:empresa):
        
        if self.primero == None:
            self.primero = nodo_empresa(empresa = empresa)

        else:
            nodoaux = self.primero

            while nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente

            nuevo_nodo = nodo_empresa(empresa=empresa)
            nodoaux.siguiente = nuevo_nodo


