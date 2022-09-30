lista_tiempos = [25,32,12,62,51,90]
tiempo_max = 0
tiempo_min = 0
for i in lista_tiempos:
    if tiempo_max < i:
        tiempo_max = i

    if tiempo_min > i or tiempo_min == 0:
        tiempo_min = i

print(tiempo_max)
print(tiempo_min)

x= "hola"
y = "luis"
z = "xd"

if (x =="hola" or z=="xd") and y == "luisss":
    print("ldfl")