from colorama import Back, Fore,Style
import xml.etree.ElementTree as ET
from Empresa import lista_empresa, empresa
from Puntos import lista_puntos, puntos
from Escritorios import lista_escritorios, escritorios
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
        while opcion != 4:

            print(Fore.CYAN+Back.CYAN+"------------Bienvenido al menu principal------------"+Back.RESET)
            print("\n")
            print(Fore.CYAN+"1. Configuración de Empresas")
            print("2. Selección de empresa y manejos de puntos de atención")
            print("4. Salir")
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



    #selección de empresa

    def manejo_empresa(self):
        opcion = ""

        while opcion !=2:
            print(Fore.MAGENTA+Back.MAGENTA+"-------Bienvenido al menú de selección de empresa-------"+Back.RESET)
            print("\n")
            print(Fore.MAGENTA+"1. Elegir empresa")
            print("2. Salir")
            print("\n")
            print("------Seleccione una opcion-------")
            opcion = int(input())


    #Manejo de puntos

    

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


                transaccion_nueva = transacciones(transaccion.attrib["id"], transaccion.find("nombre").text,transaccion.find("tiempoAtencion").text)
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

            transaccion_nueva = transacciones(id_transaccion, nombre_transaccion, tiempo)
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
                punto_buscado.puntos.escritorios.activar_escritorios()

            for cliente in config_inicial.iter("cliente"):
                
                cliente_nuevo = clientes(cliente.attrib["dpi"],cliente.find("nombre").text)
                punto_buscado.puntos.cliente.agregar(cliente_nuevo)

                for transaccion in cliente.iter("transaccion"):
                    transaccion_buscada = empresa_buscada.empresa.transacciones.buscar_transaccion(transaccion.attrib["idTransaccion"])
                    nueva_transaccion = transacciones(transaccion_buscada.transacciones.id, transaccion_buscada.transacciones.nombre, transaccion_buscada.transacciones.minutos,"luis")
                    cliente_nuevo.transacciones.agregar(nueva_transaccion)

            #punto_buscado.puntos.cliente.
            #punto_buscado.puntos.escritorios.imprimir()

            #print(punto_buscado.puntos.nombre)




        
                

           



        
menu()
