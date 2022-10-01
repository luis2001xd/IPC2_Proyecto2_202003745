
from Clientes import lista_clientes, clientes
class escritorios:
    def __init__(self,id,identificacion,encargado,estado):
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = estado
        self.cliente = lista_clientes()
        self.tiempo = 0
        self.tiempo_min = 0
        self.tiempo_max = 0
        self.contador_max = 1
        self.contador_min = 1
        

    
    def calcular_tiempo(self,tiempo):
        self.tiempo += tiempo
        return self.tiempo


    def calcular_max(self,tiempo):
        if self.contador_max == 1:
            self.tiempo_max = tiempo
            self.contador_max+=1
        
        else:
            if self.tiempo_max < tiempo:
                self.tiempo_max = tiempo

        

    def calcular_min(self,tiempo):
        if self.contador_min == 1:
            self.tiempo_min = tiempo
            self.contador_min+=1

        else: 
            if self.tiempo_min > tiempo:
                self.tiempo_min = tiempo

    def promedio(self):
        pass



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
            cadena_tiempos = "Tiempo minimo:"+str(nodoaux.escritorios.tiempo_min)+"Tiempo maximo:"+str(nodoaux.escritorios.tiempo_max)
    
            print("ID del escritorio:",nodoaux.escritorios.id,", Identificación del escritorio:",nodoaux.escritorios.identificacion,", Encargado del escritorio:",nodoaux.escritorios.encargado,nodoaux.escritorios.estado,nodoaux.escritorios.tiempo,cadena_tiempos)
            print("Clientes atendidos en este escritorio:")
            nodoaux.escritorios.cliente.imprimir()
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


    def imprimir_tiempos(self):
        nodoaux = self.primero

        while nodoaux != None:
            print("Tiempo del escritorios: ",nodoaux.escritorios.tiempo, "Estado del escritorio: ",nodoaux.escritorios.estado)
            nodoaux = nodoaux.siguiente

    

    def retornar_para_atender(self):

        nodoaux = self.primero
        tiempo_menor = 0
        id = ""

        while nodoaux!= None:
            if nodoaux.escritorios.estado == "activado":
                tiempo_menor = nodoaux.escritorios.tiempo

                break
            nodoaux = nodoaux.siguiente
        


        while nodoaux != None:

            if nodoaux.escritorios.tiempo < tiempo_menor and nodoaux.escritorios.estado == "activado":
                
                tiempo_menor = nodoaux.escritorios.tiempo
            nodoaux = nodoaux.siguiente

        escritorio_elegido = self.retornar_con_menor(tiempo_menor)
        escritorio_elegido.escritorios.estado = "desactivado"
        return escritorio_elegido

        
        

       

    def retornar_con_menor(self,tiempo_menor):
        
        nodoaux = self.primero

        while nodoaux.escritorios.tiempo != tiempo_menor :
            if nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente

            else:
                return None

        return nodoaux


        

              

