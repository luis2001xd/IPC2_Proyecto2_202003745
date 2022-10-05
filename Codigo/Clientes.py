from Transacciones import lista_transacciones

class clientes:
    def __init__(self,dpi,nombre,estado):
        self.dpi = dpi
        self.nombre = nombre
        self.estado = estado
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
            print("Nombre del cliente:",nodoaux.cliente.nombre,", Estado:",nodoaux.cliente.estado,", Dpi:",nodoaux.cliente.dpi)
            nodoaux = nodoaux.siguiente



    def retornar_sin_atender(self):

        nodoaux = self.primero

        if self.primero == None:
            return None

        while nodoaux.cliente.estado != "Sin atender":
            if nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente
            else: 
                print ("Todos los clientes han sido atendidos")
                return None


        return nodoaux

    def contar_sin_atender(self):
        contador = 0
        nodoaux = self.primero

        while nodoaux != None:
            if nodoaux.cliente.estado == "Sin atender":
                contador += 1
            nodoaux = nodoaux.siguiente

        return contador


    def contar_atendidos(self):
        nodoaux = self.primero
        contador_atendidos = 0

        while nodoaux != None:
            if nodoaux.cliente.estado == "atendido":
                contador_atendidos+=1
            nodoaux = nodoaux.siguiente

        return contador_atendidos

    
    def buscar_por_dpi(self,dpi):
        nodoaux = self.primero

        while nodoaux.cliente.dpi != dpi:
            if nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente

            else:
                return None

        return nodoaux


    def contar_cliente(self):
        nodoaux = self.primero
        contador_clientes = 0

        while nodoaux != None:
            contador_clientes += 1
            nodoaux = nodoaux.siguiente

        return contador_clientes


    def graficar_cliente(self):
        nodoaux = self.primero

        cadena = "subgraph cluster_0 {\n"
        while nodoaux!= None:
            if nodoaux.cliente.estado == "atendido":
                cadena+=nodoaux.cliente.dpi+"[label="+"\""+nodoaux.cliente.nombre+"\" color = red]\n"
            else:
                cadena+=nodoaux.cliente.dpi+"[label="+"\""+nodoaux.cliente.nombre+"\" color = blue]\n"

        cadena+="}"


    


    

                

