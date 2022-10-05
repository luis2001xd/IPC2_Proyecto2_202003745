from Clientes import lista_clientes
class escritorios_desactivados:
    def __init__(self,id,identificacion,encargado,estado,cliente = None):
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
        self.cantidad_clientes = 0
        self.promedio = 1
       
        

    
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

    def calcular_promedio(self):
        self.cantidad_clientes+=1
        self.promedio = self.tiempo / self.cantidad_clientes
        



class nodo_escritorios:
    def __init__(self, escritorios : escritorios_desactivados, siguiente = None,anterior = None):
        self.escritorios = escritorios
        self.siguiente = siguiente
        self.anterior = anterior

class lista_desactivados:

    def __init__(self):
        self.primero = None
        self.numero_activos = 0
        self.cadena_activados = ""
        self.cadena_desactivados = ""

    def agregar(self, escritorio : escritorios_desactivados):

    
        if self.primero == None:
            self.primero = nodo_escritorios(escritorios=escritorio,siguiente=None)

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
    
    
            print("ID del escritorio:",nodoaux.escritorios.id,", Encargado del escritorio:",\
                nodoaux.escritorios.encargado,",Tiempo minimo:",nodoaux.escritorios.tiempo_min,",Tiempo máximo:",nodoaux.escritorios.tiempo_max,\
                    ", Promedio de tiempo:",nodoaux.escritorios.promedio,", Número de clientes atendidos: ",nodoaux.escritorios.cliente.contar_cliente())
            print("\nClientes atendidos en este escritorio \n")
            nodoaux.escritorios.cliente.imprimir()
            nodoaux = nodoaux.siguiente
            print("\n")
            x+=1

    


    def activar_por_id(self,id):
        nodoaux = self.primero

        while nodoaux.escritorios.id != id:
            if nodoaux.siguiente != None:
                nodoaux = nodoaux.siguiente
            else:
                return None

        nodoaux.escritorios.estado = "activado"
        return nodoaux
         

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




    def imprimir_tiempos(self):
        nodoaux = self.primero

        while nodoaux != None:
            print("Tiempo del escritorios: ",nodoaux.escritorios.tiempo, "Estado del escritorio: ",nodoaux.escritorios.estado)
            nodoaux = nodoaux.siguiente

    

    def eliminar(self, id):

        nodoaux = self.primero

        if self.primero == None:
            print("Todos los escritorios de servicio han sido activados")
            return None

        while nodoaux != None:
            if nodoaux.escritorios.id == id:
                break
            else:
                nodoaux = nodoaux.siguiente
        nodo_secundario = nodoaux
        if nodoaux == self.primero:
            self.primero = nodoaux.siguiente
            nodoaux.anterior = None
            
        else:
            if nodoaux.siguiente == None:
                nodoaux = nodoaux.anterior
                nodoaux.siguiente = None
            else:
                nodoaux.siguiente.anterior = nodoaux.anterior
                nodoaux.anterior.siguiente = nodoaux.siguiente

            

        return nodo_secundario



    def activar(self):

        nodoaux = self.primero

        if self.primero == None:
            return None
            
        while nodoaux.siguiente != None:
            nodoaux = nodoaux.siguiente


        while nodoaux != None:
            if nodoaux.escritorios.estado == "desactivado":
                nodoaux.escritorios.estado = "activado"
                break

            else: 
                nodoaux = nodoaux.anterior

        if nodoaux == None:
            print("Ya no hay escritorios por activar")
            return None

        else:
            return nodoaux

    
    def tiempo_promedio(self):
        nodoaux = self.primero
        tiempo_promedio = 0

        while nodoaux != None:
            tiempo_promedio += nodoaux.escritorios.promedio
            nodoaux = nodoaux.siguiente

        return tiempo_promedio
            

    def retornar_desactivados(self):
        nodoaux = self.primero
        desactivados = 0

        while nodoaux != None:
            desactivados+=1
            nodoaux = nodoaux.siguiente

        return desactivados
    


