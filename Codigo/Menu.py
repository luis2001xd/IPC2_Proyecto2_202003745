
from colorama import Back, Fore,Style
import xml.etree.ElementTree as ET
from Empresa import lista_empresa, empresa
from Puntos import lista_puntos, puntos
from Escritorios import lista_escritorios, escritorios,nodo_escritorios
from Transacciones import lista_transacciones, transacciones
from Clientes import lista_clientes, clientes
from tkinter import messagebox
class menu:
    def __init__(self, empresa = None):

        self.menu_principal()

        self.empresa = None

        

        

    def menu_principal(self):

        self.empresa = lista_empresa()
        

        opcion = " "
        print("\n")
        
        #Menú principal
        while opcion != 3:

            print(Fore.CYAN+Back.CYAN+"------------Bienvenido al menu principal------------"+Back.RESET)
            print("\n")
            print(Fore.CYAN+"1. Configuración de Empresas")
            print("2. Selección de empresa y manejos de puntos de atención")
            print("3. Salir")
            print("\n")
            print("------Seleccione una opcion-------")
            opcion = int(input())


            if opcion == 1:
                self.configuracion_empresas()

            if opcion == 2:
                self.manejo_empresa()



            
            

    #configuración de alguna empresa

    def configuracion_empresas(self):
        
        opcion = ""

        while opcion !=5:
            print(Fore.GREEN+Back.GREEN+"-------Bienvenido al menú de configuración de la empresa-------"+Back.RESET)
            print("\n")
            print(Fore.GREEN+"1. Limpiar sistema")
            print("2. Cargar Archivo de configuración del sistema")
            print("3. Crear nueva empresa")
            print("4. Cargar archivo con configuración inicial para la prueba")
            print("5. Salir")
            print("\n")
            print("------Seleccione una opcion-------")
            opcion = int(input())

            if opcion == 1:

                print(self.empresa.limpiar_sistema())


            if opcion == 2:
                ruta = input("Introduzca la ruta del archivo: \n")
                self.cargar_configuracion(ruta)
                

            if opcion ==3:

                self.crear_empresa()

            
            if opcion == 4:

                ruta = input("Introduzca la ruta del archivo: \n")
                self.cargar_simulacion(ruta)
                print("Archivo leído con éxito")





    #Manejo y selección de empresas y puntos

    def manejo_empresa(self):
        opcion = ""

        while opcion !=2:
            print(Fore.BLUE+Back.BLUE+"-------Bienvenido al menú de selección de empresa-------"+Back.RESET)
            print("\n")
            print(Fore.BLUE+"1. Elegir empresa")
            print("2. Salir")
            print("\n")
            print("------Seleccione una opcion-------")
            opcion = int(input())

            if opcion == 1:
                self.empresa.imprimir()
                print("\n")
                opcion2 = input("Introduzca el ID de la empresa que desea manejar: \n")
                empresa_buscada = self.empresa.buscar_id(opcion2)

                if empresa_buscada == None:
                    print("No se encontró la empresa")
                else:
                    empresa_buscada.empresa.puntos_atencion.imprimir()
                    print("\n")

                    opcion3 = input("Introduzca el ID del punto que desea manejar: \n")
                    punto_buscado = empresa_buscada.empresa.puntos_atencion.buscar_punto(opcion3)

                    if punto_buscado == None:
                        print("No se encontró el punto en la empresa ")
                    
                    else: 
                        self.manejo_puntos(punto_buscado,empresa_buscada)
                        
                        



    


    def manejo_puntos(self, punto_buscado,empresa_buscada):
        opcion = ""
        punto_buscado = punto_buscado
        empresa_buscada = empresa_buscada
       
        while opcion !=7:
            print(Fore.BLUE+Back.BLUE+"-------Bienvenido al menú de manejo de puntos-------"+Back.RESET)
            print("\n")
            print(Fore.BLUE+"1. Ver estado del punto de atención")
            print("2. Activar escritorio de servicio")
            print("3. Desactivar Escritorio")
            print("4. Atender cliente")
            print("5. Solicitud de atención")
            print("6. Simular actividad del punto de atención")
            print("7. Salir")
            opcion = int(input())


            if opcion == 1:
                self.mostrar_puntoatencion(punto_buscado)
                

            if opcion == 2:
                self.activar_escritorio(punto_buscado)
                

            if opcion == 3:
                self.desactivar_escritorio(punto_buscado)


            if opcion == 4:
                self.atender_cliente(punto_buscado)
                print("Clientes atendidos con éxito")
                

            if opcion == 5:
                self.agregar_solcitud(punto_buscado,empresa_buscada)


            if opcion == 6:
                
                r = 1
                while r != None:
                    r = self.simular_atencion(punto_buscado)

                self.mostrar_2(punto_buscado)

            
                









    

    def cargar_configuracion(self,ruta):
        
        tree = ET.parse(ruta)
        lista_empresas = tree.getroot()

        try: 
            for nueva_empresa in lista_empresas.findall("empresa"):
            
                empresa_nueva = empresa(nueva_empresa.attrib["id"], nueva_empresa.find("nombre").text, nueva_empresa.find ("abreviatura").text)
                self.empresa.agregar(empresa_nueva)

                for lista in nueva_empresa.iter("puntoAtencion"):
            
                    punto_nuevo = puntos(lista.attrib["id"], lista.find("nombre").text,lista.find("direccion").text)
                    empresa_nueva.puntos_atencion.agregar(punto_nuevo)

                    for lista_escritorios in lista.iter("escritorio"):
                        
                        escritorio_nuevo = escritorios(lista_escritorios.attrib["id"], lista_escritorios.find("identificacion").text, lista_escritorios.find("encargado").text,"desactivado")
                        punto_nuevo.escritorios.agregar(escritorio_nuevo)
                        punto_nuevo.desactivados.agregar(escritorio_nuevo)

                for transaccion in nueva_empresa.iter("transaccion"):


                    transaccion_nueva = transacciones(transaccion.attrib["id"], transaccion.find("nombre").text,int(transaccion.find("tiempoAtencion").text))
                    empresa_nueva.transacciones.agregar(transaccion_nueva)
            
        except:
            print("Ocurrió un error, por favor revise que los campos introducidos sean correctos")

        print("Archivo leído con éxito")
        
        





    def crear_empresa(self):

        print("\n")

        print("Bienvenido a la creación de la empresa")
        
        id_empresa = input("Introduzca el id de la empresa: ")
        nombre_empresa = input("Introduzca el nombre de la empresa: ")
        abreviatura_empresa = input ("Introduzca la abreviatura de la empresa: ")
        empresa_nueva = empresa(id_empresa, nombre_empresa, abreviatura_empresa)
        self.empresa.agregar(empresa_nueva)

        n_puntos = int(input("Introduzca la cantidad de puntos de atención que desea agregar: "))

        i=1
        k=1
        print("\n")
        

        while i<=n_puntos:

            print("\n")

            print("--------Creación de punto--------")
            print("\n")

            id_punto = input("Introduzca el id del punto: ")
            nombre_punto = input ("Introduzca el nombre del punto: ")
            direccion_punto = input ("Introduzca la direccion del punto: ")

            punto_nuevo = puntos(id_punto, nombre_punto, direccion_punto)

            empresa_nueva.puntos_atencion.agregar(punto_nuevo)

            n_escritorios = int(input("Introduzca cuantos escritorios tendrá el nuevo punto: "))

            j=1

            while j<=n_escritorios:

                print("\n")
                print("--------Creacion de escritorios--------")
                print("\n")

                id_escritorio = input("Introduzca el id del escritorio: ")
                identificacion = input("Introduzca la identificacion del escritorio: ")
                encargado = input("Introduzca al encargado del escritorio: ")

                escritorio_nuevo = escritorios(id_escritorio,identificacion,encargado,"desactivado")

                punto_nuevo.escritorios.agregar(escritorio_nuevo)
                punto_nuevo.desactivados.agregar(escritorio_nuevo)

                j+=1
            
            i+=1

        print("------------------------------------------------")
        print("\n")
        n_transacciones = int(input("Introduzca el número de transacciones que desea agregar: "))

        while k<=n_transacciones:
            print("\n")
            print("--------Creación de transacciones--------")
            print("\n")

            id_transaccion = input("Introduzca el id de la transacción: ")
            nombre_transaccion = input("Introduzca el nombre de la transaccion: ")
            tiempo = input ("Introduzca el tiempo de la transaccion: ")

            transaccion_nueva = transacciones(id_transaccion, nombre_transaccion, int(tiempo))
            empresa_nueva.transacciones.agregar(transaccion_nueva)

            k+=1




    def cargar_simulacion(self,ruta):

        tree = ET.parse(ruta)
        lista_inicial = tree.getroot()
        
        for config_inicial in lista_inicial.findall("configInicial"):

            empresa_buscada = self.empresa.buscar_id(config_inicial.attrib["idEmpresa"])

            #empresa_buscada.empresa.transacciones.imprimir()

            punto_buscado = empresa_buscada.empresa.puntos_atencion.buscar_punto(config_inicial.attrib["idPunto"])

            for escritorio in config_inicial.iter("escritorio"):
                punto_buscado.puntos.escritorios.activar_por_id(escritorio.attrib["idEscritorio"])
                r = punto_buscado.puntos.desactivados.eliminar(escritorio.attrib["idEscritorio"])
                if r == None:
                    continue
                punto_buscado.puntos.activos.agregar(r.escritorios)
                

            for cliente in config_inicial.iter("cliente"):
                
                cliente_nuevo = clientes(cliente.attrib["dpi"],cliente.find("nombre").text,"Sin atender")
                punto_buscado.puntos.cliente.agregar(cliente_nuevo)

                for transaccion in cliente.iter("transaccion"):
                    transaccion_buscada = empresa_buscada.empresa.transacciones.buscar_transaccion(transaccion.attrib["idTransaccion"])
                    nueva_transaccion = transacciones(transaccion_buscada.transacciones.id, transaccion_buscada.transacciones.nombre, int(transaccion_buscada.transacciones.minutos),int(transaccion.attrib["cantidad"]))
                    cliente_nuevo.transacciones.agregar(nueva_transaccion)


            #punto_buscado.puntos.cliente.
            #punto_buscado.puntos.escritorios.imprimir()

            #print(punto_buscado.puntos.nombre)




    def activar_escritorio(self,punto_buscado):

        nodo_activado = punto_buscado.puntos.desactivados.activar()
        if nodo_activado == None:
            print("Todos los escritorios de servicio han sido activados")
            return

        punto_buscado.puntos.desactivados.eliminar(nodo_activado.escritorios.id)
        punto_buscado.puntos.activos.agregar(nodo_activado.escritorios)
        print("Información del escritorio que se activo: \n")
        print("Id del escritorio: ",nodo_activado.escritorios.id)
        print("Encergado del escritorio: ",nodo_activado.escritorios.encargado)
        print("Escritorio activado con exito")
        print("\n")




    def desactivar_escritorio(self,punto_buscado):
        
        nodo_desactivado =  punto_buscado.puntos.activos.desactivar()
        if nodo_desactivado == None:
            print("Todos los escritorios de servicio han sido desactivados")
            return

        punto_buscado.puntos.activos.eliminar(nodo_desactivado.escritorios.id)
        punto_buscado.puntos.desactivados.agregar(nodo_desactivado.escritorios)
        print("Información del escritorio que se desactivo: \n")
        print("Id del escritorio: ",nodo_desactivado.escritorios.id)
        print("Encergado del escritorio: ",nodo_desactivado.escritorios.encargado)
        print ("Escritorio desactivado con éxito")
        print("\n")




    def atender_cliente(self,punto_buscado):
        count = 1
        ciclo = punto_buscado.puntos.activos.retornar_activo()
        if ciclo == 0:
            print("No hay escritorios de servicio activos")
            return

        cadena_id = ""
        tiempo_total = 0

        while count <= ciclo:
            cliente_atendido = punto_buscado.puntos.cliente.retornar_sin_atender()
            if cliente_atendido == None:
                break
            
            else: 
                escritorio_activo = punto_buscado.puntos.activos.retornar_para_atender()
                cliente_atendido.cliente.estado = "atendido"

                escritorio_activo.escritorios.calcular_max(cliente_atendido.cliente.transacciones.calcular())
                escritorio_activo.escritorios.calcular_min(cliente_atendido.cliente.transacciones.calcular())
                escritorio_activo.escritorios.calcular_tiempo(cliente_atendido.cliente.transacciones.calcular_tiempo())

                cliente_atendido1 = punto_buscado.puntos.cliente.buscar_por_dpi(cliente_atendido.cliente.dpi)
                escritorio_activo.escritorios.cliente.agregar(cliente_atendido1.cliente)
                escritorio_activo.escritorios.calcular_promedio()

                cadena_id+=escritorio_activo.escritorios.id+","
                punto_buscado.puntos.minimo_atencion(escritorio_activo.escritorios.tiempo_min)
                punto_buscado.puntos.maximo_atencion(escritorio_activo.escritorios.tiempo_max)
                punto_buscado.puntos.total_tiempo(cliente_atendido.cliente.transacciones.calcular())

                if count == ciclo:
                    punto_buscado.puntos.maximo_espera(escritorio_activo.escritorios.tiempo)
                

            count += 1

        subcadena = ""
        punto_buscado.puntos.minimo_espera(punto_buscado.puntos.tiempo_min_atencion)
        punto_buscado.puntos.calcular_promedio_espera(punto_buscado.puntos.tiempo_max_atencion, punto_buscado.puntos.cliente.contar_cliente())
        
        

        for cadena in cadena_id:
            if cadena !=",":
                subcadena+=cadena
            
            else:
                punto_buscado.puntos.activos.activar_por_id(subcadena)
                subcadena = ""

        

    def agregar_solcitud(self,punto_buscado,empresa_buscada):

        print("Bienvenido al menú de creación de clientes")
        dpi= input("Introduzca el DPI: \n")
        nombre = input ("Introduzca el nombre del cliente: \n")

        cliente_nuevo = clientes(dpi,nombre,"Sin atender")
        punto_buscado.puntos.cliente.agregar(cliente_nuevo)
        empresa_buscada.empresa.transacciones.imprimir()

        opc = ""

        while opc != "F":
            transaccion = input("Introduzca el ID de la transacción que desea realizar: \n")
            cantidad = input ("Introduzca la cantidad que desea realizar de esta transacción: \n")
            transaccion_buscada = empresa_buscada.empresa.transacciones.buscar_transaccion(transaccion)
            nueva_transaccion = transacciones(transaccion_buscada.transacciones.id, transaccion_buscada.transacciones.nombre, int(transaccion_buscada.transacciones.minutos),int(cantidad))
            cliente_nuevo.transacciones.agregar(nueva_transaccion)

            print("Desea agregar otra transacción? Si desea salir del menú presione F")
            opc = input()




    def simular_atencion(self,punto_buscado):
        count = 1
        ciclo = punto_buscado.puntos.activos.retornar_activo()
        if ciclo == 0:
            print("No hay escritorios de servicio activos")
            return

        cadena_id = ""

        while count <= ciclo:
            cliente_atendido = punto_buscado.puntos.cliente.retornar_sin_atender()
            if cliente_atendido == None:
                x = None
                break
            
            else: 
                x = 1
                escritorio_activo = punto_buscado.puntos.activos.retornar_para_atender()
                cliente_atendido.cliente.estado = "atendido"

                escritorio_activo.escritorios.calcular_max(cliente_atendido.cliente.transacciones.calcular())
                escritorio_activo.escritorios.calcular_min(cliente_atendido.cliente.transacciones.calcular())
                escritorio_activo.escritorios.calcular_tiempo(cliente_atendido.cliente.transacciones.calcular_tiempo())

                cliente_atendido1 = punto_buscado.puntos.cliente.buscar_por_dpi(cliente_atendido.cliente.dpi)
                escritorio_activo.escritorios.cliente.agregar(cliente_atendido1.cliente)
                escritorio_activo.escritorios.calcular_promedio()

                cadena_id+=escritorio_activo.escritorios.id+","
                punto_buscado.puntos.minimo_atencion(escritorio_activo.escritorios.tiempo_min)
                punto_buscado.puntos.maximo_atencion(escritorio_activo.escritorios.tiempo_max)
                punto_buscado.puntos.total_tiempo(cliente_atendido.cliente.transacciones.calcular())

                if count == ciclo:
                    punto_buscado.puntos.maximo_espera(escritorio_activo.escritorios.tiempo)

            count += 1

        subcadena = ""
        punto_buscado.puntos.minimo_espera(punto_buscado.puntos.tiempo_min_atencion)
        punto_buscado.puntos.calcular_promedio_espera(punto_buscado.puntos.tiempo_max_atencion, punto_buscado.puntos.cliente.contar_cliente())
        

        for cadena in cadena_id:
            if cadena !=",":
                subcadena+=cadena
            
            else:
                punto_buscado.puntos.activos.activar_por_id(subcadena)
                subcadena = ""

        return x

    def tiempo_promedio(self,punto_buscado):
        ciclo = punto_buscado.puntos.activos.retornar_activo()
        tiempo_promedio_activos = punto_buscado.puntos.activos.tiempo_promedio()
        tiempo_promedio_desactivados = punto_buscado.puntos.desactivados.tiempo_promedio()
        tiempo_total = tiempo_promedio_activos + tiempo_promedio_desactivados
        punto_buscado.puntos.calcular_promedio(tiempo_total,ciclo)


    def mostrar_puntoatencion(self,punto_buscado):
        print("----Información del punto de atención-----")
        print("ID del punto de atención:", punto_buscado.puntos.id)
        print("Cantidad de escritorios activos:", punto_buscado.puntos.activos.retornar_activo())
        print("Cantidad de escritorios inactivos:", punto_buscado.puntos.desactivados.retornar_desactivados())
        print("Clientes en espera de atención:",punto_buscado.puntos.cliente.contar_sin_atender())
        print("")
        print("Tiempos de atención:")
        print("Tiempo minímo de atención:",punto_buscado.puntos.tiempo_min_atencion)
        print("Tiempo máximo de atención:",punto_buscado.puntos.tiempo_max_atencion)
        self.tiempo_promedio(punto_buscado)
        print("Tiempo promedio de atencion:",punto_buscado.puntos.tiempo_prom_atencion)
        print("\n")
        print("Tiempos de espera:")
        print("Tiempo minímo de espera:",punto_buscado.puntos.tiempo_min_espera)
        print("Tiempo máximo de espera:",punto_buscado.puntos.tiempo_max_espera)
        print("Tiempo promedio de espera:",punto_buscado.puntos.tiempo_prom_espera)
        print("\n Información de los escritorios activos del punto de atención: \n")
        punto_buscado.puntos.activos.imprimir()


    def mostrar_2(self,punto_buscado):
        print("----Información del punto de atención-----")
        print("ID del punto de atención:", punto_buscado.puntos.id)
        print("Cantidad de escritorios activos:", punto_buscado.puntos.activos.retornar_activo())
        print("Cantidad de escritorios inactivos:", punto_buscado.puntos.desactivados.retornar_desactivados())
        print("Clientes en espera de atención:",punto_buscado.puntos.cliente.contar_sin_atender())
        print("")
        print("Tiempos de atención:")
        print("Tiempo minímo de atención:",punto_buscado.puntos.tiempo_min_atencion)
        print("Tiempo máximo de atención:",punto_buscado.puntos.tiempo_max_atencion)
        self.tiempo_promedio(punto_buscado)
        print("Tiempo promedio de atencion:",punto_buscado.puntos.tiempo_prom_atencion)
        print("\n")
        print("Tiempos de espera:")
        print("Tiempo minímo de espera:",punto_buscado.puntos.tiempo_min_espera)
        print("Tiempo máximo de espera:",punto_buscado.puntos.tiempo_max_espera)
        print("Tiempo promedio de espera:",punto_buscado.puntos.tiempo_prom_espera)
        print("\n Información de los escritorios activos del punto de atención: \n")
        punto_buscado.puntos.activos.imprimir()
        print("\n Información de los escritorios inactivos del punto de atención: \n")
        punto_buscado.puntos.desactivados.imprimir()






        

                

         
        



        

        


        
                

           



        
menu()
