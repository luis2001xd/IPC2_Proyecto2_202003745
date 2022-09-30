
from Clientes import lista_clientes, clientes
class escritorios:
    def __init__(self,id,identificacion,encargado,estado):
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = estado
        self.cliente = lista_clientes()
        self.tiempo = 0

    
    def calcular_tiempo(self,tiempo):
        self.tiempo += tiempo
        return self.tiempo



class nodo_escritorios:
    def __init__(self, escritorios : escritorios, siguiente = None,anterior = None):
        self.escritorios = escritorios
        self.siguiente = siguiente
        self.anterior = anterior

class lista_escritorios:

    def __init__(self):
        self.primero = None
        self.numero_activos = 0

    def agregar(self, escritorio : escritorios):

        if self.primero == None:
            self.primero = nodo_escritorios(escritorios=escritorio)

        else: 
            nodoaux = self.primero

            while nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente

            nuevo_escritorio = nodo_escritorios (escritorios = escritorio, siguiente = None)
            nodoaux.siguiente = nuevo_escritorio
            nuevo_escritorio.anterior = nodoaux


    def imprimir(self):

        nodoaux = self.primero
        x=1
        while nodoaux != None:
            
            print("------Información de escritorio No."+str(x)+"-------------")
            print("ID del escritorio:",nodoaux.escritorios.id,", Identificación del escritorio:",nodoaux.escritorios.identificacion,", Encargado del escritorio:",nodoaux.escritorios.encargado,nodoaux.escritorios.estado)
            print("Clientes: ", nodoaux.escritorios.cliente.imprimir())
            nodoaux = nodoaux.siguiente
            x+=1

    def activar_por_id(self,id):
        nodoaux = self.primero

        while nodoaux.escritorios.id != id:
            if nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente
            else:
                return None

        nodoaux.escritorios.estado = "activado"
                


        


    def activar_ultimo(self):
        nodoaux = self.primero

        while nodoaux.siguiente != None:
            nodoaux = nodoaux.siguiente


        while nodoaux != None:
            if nodoaux.escritorios.estado == "desactivado":
                nodoaux.escritorios.estado = "activado"
                return


            else: 
                nodoaux = nodoaux.anterior


    def desactivar_ultimo(self):
        nodoaux = self.primero

        while nodoaux.siguiente != None:
            nodoaux = nodoaux.siguiente


        while nodoaux != None:
            if nodoaux.escritorios.estado == "activado":
                nodoaux.escritorios.estado = "desactivado"
                return


            else: 
                nodoaux = nodoaux.anterior

    def retornar_activo(self):
        nodoaux = self.primero

        self.numero_activos = 0

        while nodoaux != None:
            if nodoaux.escritorios.estado == "activado":
                self.numero_activos += 1

            nodoaux = nodoaux.siguiente
        
        return self.numero_activos

    
    def retornar_para_atender(self):

        nodoaux = self.primero

        while nodoaux.escritorios.estado != "activado":
            nodoaux = nodoaux.siguiente

        nodoaux.escritorios.estado = "desactivado"

        return nodoaux

    def retornar_para_atender(self):

        nodoaux = self.primero
        tiempo_menor = 0

        while nodoaux != None:
            
            if (nodoaux.escritorios.tiempo < tiempo_menor or tiempo_menor == 0) and nodoaux.escritorios.estado == "activado":
                
                tiempo_menor = nodoaux.escritorios.tiempo
                nodoaux.escritorios.estado = "desactivado"
            nodoaux = nodoaux.siguiente

        escritorio_elegido = self.retornar_con_menor(tiempo_menor)
        return escritorio_elegido

        
        

       

    def retornar_con_menor(self,tiempo):
        
        nodoaux = self.primero

        while nodoaux.escritorios.tiempo != tiempo:
            if nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente

            else:
                return None

        return nodoaux


        

              

