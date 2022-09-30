from colorama import Back, Fore,Style
import xml.etree.ElementTree as ET
from Empresa import lista_empresa, empresa
from Puntos import lista_puntos, puntos
from Escritorios import lista_escritorios, escritorios,nodo_escritorios
from Transacciones import lista_transacciones, transacciones
from Clientes import lista_clientes, clientes

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
                        self.manejo_puntos(punto_buscado)



    


    def manejo_puntos(self, punto_buscado):
        opcion = ""
        punto_buscado = punto_buscado
       
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

            if opcion == 2:
                self.activar_escritorio(punto_buscado)
                punto_buscado.puntos.escritorios.imprimir()

            if opcion == 3:
                self.desactivar_escritorio(punto_buscado)
                punto_buscado.puntos.escritorios.imprimir()


            if opcion == 4:
                self.atender_cliente(punto_buscado)
                punto_buscado.puntos.escritorios.imprimir()
                print("------------------")
                punto_buscado.puntos.cliente.imprimir()

            if opcion == 5:
                punto_buscado.puntos.escritorios.imprimir()
                









    

    def cargar_configuracion(self,ruta):
        
        tree = ET.parse(ruta)
        lista_empresas = tree.getroot()

        for nueva_empresa in lista_empresas.findall("empresa"):
        
            empresa_nueva = empresa(nueva_empresa.attrib["id"], nueva_empresa.find("nombre").text, nueva_empresa.find ("abreviatura").text)
            self.empresa.agregar(empresa_nueva)

            for lista in nueva_empresa.iter("puntoAtencion"):
        
                punto_nuevo = puntos(lista.attrib["id"], lista.find("nombre").text,lista.find("direccion").text)
                empresa_nueva.puntos_atencion.agregar(punto_nuevo)

                for lista_escritorios in lista.iter("escritorio"):
                    
                    escritorio_nuevo = escritorios(lista_escritorios.attrib["id"], lista_escritorios.find("identificacion").text, lista_escritorios.find("encargado").text,"desactivado")
                    punto_nuevo.escritorios.agregar(escritorio_nuevo)

            for transaccion in nueva_empresa.iter("transaccion"):


                transaccion_nueva = transacciones(transaccion.attrib["id"], transaccion.find("nombre").text,int(transaccion.find("tiempoAtencion").text))
                empresa_nueva.transacciones.agregar(transaccion_nueva)





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

            for escritorios in config_inicial.iter("escritorio"):
                punto_buscado.puntos.escritorios.activar_por_id(escritorios.attrib["idEscritorio"])

            for cliente in config_inicial.iter("cliente"):
                
                cliente_nuevo = clientes(cliente.attrib["dpi"],cliente.find("nombre").text,"Sin atender")
                punto_buscado.puntos.cliente.agregar(cliente_nuevo)

                for transaccion in cliente.iter("transaccion"):
                    transaccion_buscada = empresa_buscada.empresa.transacciones.buscar_transaccion(transaccion.attrib["idTransaccion"])
                    nueva_transaccion = transacciones(transaccion_buscada.transacciones.id, transaccion_buscada.transacciones.nombre, int(transaccion_buscada.transacciones.minutos),int(transaccion.attrib["cantidad"]))
                    cliente_nuevo.transacciones.agregar(nueva_transaccion)

            #punto_buscado.puntos.cliente.
            punto_buscado.puntos.escritorios.imprimir()

            #print(punto_buscado.puntos.nombre)




    def activar_escritorio(self,punto_buscado):

        punto_buscado.puntos.escritorios.activar_ultimo()

        print("Escritorio activado con exito")

    def desactivar_escritorio(self,punto_buscado):
        
        punto_buscado.puntos.escritorios.desactivar_ultimo()
        print ("Escritorio desactivado con éxito")

    def atender_cliente(self,punto_buscado):
        
        

        count = 1
        ciclo = punto_buscado.puntos.escritorios.retornar_activo()


        cadena_id = ""

        while count <= ciclo:
            cliente_atendido = punto_buscado.puntos.cliente.retornar_sin_atender()
            escritorio_activo = punto_buscado.puntos.escritorios.retornar_para_atender()
            print(escritorio_activo)
            if cliente_atendido == None:
                print("xd") 
                break
            else: 
                cliente_atendido.cliente.estado = "atendido"
                print(escritorio_activo.escritorios.estado,":")
                print(escritorio_activo.escritorios.calcular_tiempo(cliente_atendido.cliente.transacciones.calcular_tiempo()))
                cliente_atendido1 = clientes(cliente_atendido.cliente.dpi,cliente_atendido.cliente.nombre,cliente_atendido.cliente.estado)
                escritorio_activo.escritorios.cliente.agregar(cliente_atendido1)
                print("--------------------")
                cadena_id+=escritorio_activo.escritorios.id+","
                count += 1

        subcadena = ""

        for cadena in cadena_id:
            if cadena !=",":
                subcadena+=cadena
            
            else:
                punto_buscado.puntos.escritorios.activar_por_id(subcadena)
                subcadena = ""

                

        print(cadena_id) 
        



        

        


        
                

           



        
menu()
