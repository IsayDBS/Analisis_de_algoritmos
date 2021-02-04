import sys
import random

def BusquedaBinaria(array,z):
    izq = 0
    der = len(array) - 1
    mid = 0

    while izq <= der:
        mid = (der + izq) // 2
        if array[mid] < z:
            izq = mid + 1
        elif array[mid] > z:
            der = mid - 1
        else:
            return mid
    return -1

def arreglo(tamanio):
    array = [None]*tamanio
    array[0] = random.randint(0,10)
    for i in range(1,tamanio):
        array[i] = array[0]
    while array[0] >= array[tamanio-1]:
        for x in range(1,tamanio):
            array[x] = numero(array[x-1])
    return array,random.randint(array[0],array[tamanio-1])

def numero(antecesor):
    x = random.randint(0,2)
    if x == 0:
        return antecesor-1
    elif x == 1:
        return antecesor
    else: #x==2
        return antecesor+1

tamanio = int(sys.argv[1])
if tamanio <= 1:
    print("El valor no es valido")
else:
    array,z = arreglo(tamanio)
    print("Arreglo: " + str(array))
    print("Valor a buscar: " + str(z))
    print("Resultado:" + str(BusquedaBinaria(array,z)))
