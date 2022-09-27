from colorama import Back, Fore,Style

class menu:
    def __init__(self):
        self.menu_principal()

    def menu_principal(self):

        opcion = " "
        print("\n")
        
        #Menú principal
        while opcion != 4:

            print(Fore.CYAN+Back.CYAN+"------------Bienvenido al menu principal------------"+Back.RESET)
            print("\n")
            print(Fore.CYAN+"1. Configuración de Empresas")
            print("2. Selección de empresa y puntos de atención")
            print("3. Manejo de puntos de atención ")
            print("4. Salir")
            print("\n")
            print("------Seleccione una opcion-------")
            opcion = int(input())


            if opcion == 1:
                self.configuracion_empresas()

            if opcion == 2:
                self.seleccion_empresa()

            if opcion == 3:
                self.manejo_puntos()


            
            

    #configuración de alguna empresa

    def configuracion_empresas(self):
        opcion = ""

        while opcion !=5:
            print(Fore.GREEN+Back.GREEN+"-------Bienvenido al menú de configuración de la empresa-------"+Back.RESET)
            print("\n")
            print(Fore.GREEN+"1. Limpiar sistema")
            print("2. Cargar Archivo")
            print("3. Crear nueva empresa")
            print("4. Cargar archivo con configuración inicial para la prueba")
            print("5. Salir")
            print("\n")
            print("------Seleccione una opcion-------")
            opcion = int(input())

            if opcion == 1:
                print("Este es el menú de configuracion")



    #selección de empresa

    def seleccion_empresa(self):
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

    def manejo_puntos(self):

        opcion = ""

        while opcion !=5:
            print(Fore.BLUE+Back.BLUE+"-------Bienvenido al menú de configuración de la empresa-------"+Back.RESET)
            print("\n")
            print(Fore.BLUE+"1. Limpiar sistema")
            print("2. Cargar Archivo")
            print("3. Crear nueva empresa")
            print("4. Cargar archivo con configuración inicial para la prueba")
            print("5. Salir")
            print("\n")
            print("------Seleccione una opcion-------")
            opcion = int(input())

            if opcion == 1:
                print("Este es el menú de configuracion")

menu()
