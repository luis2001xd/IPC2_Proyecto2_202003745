lista_tiempos = [25,32,12,62,51,90]
tiempo_max = 0
tiempo_min = 0
menor = lista_tiempos[0]

for i in lista_tiempos:
    if menor > i:
        menor = i

print (menor)