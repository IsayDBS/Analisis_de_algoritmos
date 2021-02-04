def seleccionk(arreglo, low, high, k):
    pivote = partition(arreglo,low,high)
    if pivote==k:
        return arreglo[k]
    elif pivote<k:
        return seleccionk(arreglo,pivote+1,high,k)
    elif pivote>k:
        return seleccionk(arreglo,low,pivote-1,k)
    return -1

def partition(arreglo,low,high):
    pivote = arreglo[high]
    i = low-1
    j = low
    for x in range(j,len(arreglo)):
        if pivote > arreglo[x]:
            i=i+1
            temp = arreglo[i]
            arreglo[i] = arreglo[x]
            arreglo[x] = temp
    temp = arreglo[i+1]
    arreglo[i+1] = arreglo[high]
    arreglo[high] = temp
    return i+1

arreglo=[10,9,2,4,5,6,7,1]
print(seleccionk(arreglo,0,len(arreglo)-1,1))
