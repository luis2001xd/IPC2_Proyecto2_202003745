from Puntos import lista_puntos
from Transacciones import lista_transacciones
class empresa:
    def __init__(self,id,nombre,abreviatura):
        self.nombre = nombre
        self.id = id
        self.abreviatura = abreviatura
        self.puntos_atencion = lista_puntos()
        self.transacciones = lista_transacciones()



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


    def imprimir(self):
        nodoaux = self.primero

        while nodoaux != None:
            print("-------------------------------------------------------------------------------------------------------------")
            print("----Información de la empresa----")
            print("ID de la empresa:",nodoaux.empresa.id,", Nombre de la empresa:",nodoaux.empresa.nombre,", Abreviatura de la empresa:",nodoaux.empresa.abreviatura)
            print("-----Información de los puntos de la empresa-----")
            print("\n")
            nodoaux.empresa.puntos_atencion.imprimir()

            print("-----Información de las transacciones-----")
            print("\n")
            nodoaux.empresa.transacciones.imprimir()
            print("-------------------------------------------------------------------------------------------------------------")
            print("\n")
            nodoaux = nodoaux.siguiente


    def limpiar_sistema(self):
        
        self.primero = None

        return ("Sistema limpiado con éxito")


    def buscar_id(self, id):
        nodoaux = self.primero

        while nodoaux.empresa.id != id:

            if nodoaux.siguiente!= None:
                nodoaux = nodoaux.siguiente

            else:
                print("Empresa no encontrada")
                return None
        
        print("Encontrado")
        return nodoaux
        


