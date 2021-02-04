import sys
import os.path

class colaPrioridad():
    def __init__(self):
        self.minHeap = MinHeap()

    def inserta(self,key,value):
        self.minHeap.push(key,value)

    def encuentraMin(self):
        return self.minHeap.peek()

    def borraMin(self):
        temp = self.minHeap.pop()

    def vacio(self):
        return self.minHeap.esVacia()

    def elimina(self,key):
        self.minHeap.eliminaPorEtiqueta(key)

    def minQ(self):
        return self.minHeap.peek()

    def decrementaLlave(self,key,value):
        x = self.minHeap.encuentraValor(key)
        if x == -1:#No encontro el valor, por lo tanto no se hace nada
            return
        #if value < self.minHeap[x][1]:
        self.minHeap.cambioValor(x,value)



class MinHeap:
    def __init__(self):
        self.heap = [] #son del tipo ['etiqueta',distancia]

    def esVacia(self):
        if self.heap == []:
            return True
        return False

    def getPadre(self, i):
        return int((i-1)/2)

    def getIzquierdo(self, i):
        return 2*i+1

    def getDerecho(self, i):
        return 2*i+2

    def tienePadre(self, i):
        return self.getPadre(i) < len(self.heap)

    def tieneIzquierdo(self, i):
        return self.getIzquierdo(i) < len(self.heap)

    def tieneDerecho(self, i):
        return self.getDerecho(i) < len(self.heap)

    def push(self, etiqueta,llave):
        self.heap.append([etiqueta,llave])
        self.heapify(len(self.heap) - 1)

    def pop(self):
        if self.esVacia():
            return None
        if len(self.heap) == 1:
            temp = self.heap[0]
            self.heap = []
            return temp
        temp = self.heap[0]
        ultimo = len(self.heap) - 1
        self.heap[0] = self.heap[ultimo]
        del self.heap[ultimo]
        self.heapifyPop(0)
        return temp

    def hijoMin(self,i):
        derecho = self.getDerecho(i)
        izquierdo = self.getIzquierdo(i)
        tamanio = len(self.heap)
        if derecho < tamanio and izquierdo < tamanio:
            if self.heap[izquierdo][1] < self.heap[derecho][1]:
                return izquierdo
            else:
                return derecho
        elif derecho < tamanio and izquierdo >= tamanio:
            return derecho
        elif izquierdo < tamanio and derecho >= tamanio:
            return izquierdo
        else:#no tiene hijos
            return -1

    def heapifyPop(self,posicion):#[etiqueta,valor]
        hijomin = self.hijoMin(posicion)
        #posicion no tiene hijos, por lo tanto ya acaba
        if hijomin == -1:
            return
        #tiene al menos un hijo
        if self.heap[hijomin][1] < self.heap[posicion][1]:
            self.heap[hijomin],self.heap[posicion] = self.heap[posicion],self.heap[hijomin]
            self.heapifyPop(hijomin)

    def peek(self):
        if self.esVacia():
            return None
        return self.heap[0]

    def heapify(self, i):
        while(self.tienePadre(i) and self.heap[i][1] < self.heap[self.getPadre(i)][1]):
            self.heap[i], self.heap[self.getPadre(i)] = self.heap[self.getPadre(i)], self.heap[i]
            i = self.getPadre(i)

    def imprimeHeap(self):
        print(self.heap)

    def encuentraValor(self,etiqueta):
            for x in range(0,len(self.heap)):
                if self.heap[x][0] == etiqueta:
                    return x
            return -1

    def eliminaPorEtiqueta(self,etiqueta):
        x = self.encuentraValor(etiqueta)
        self.heap[x],self.heap[-1] = self.heap[-1],self.heap[x]
        del self.heap[-1]
        if self.tienePadre(x):
            if self.heap[x][1] < self.heap[self.getPadre(x)][1]:
                self.heapify(x)
                return
        self.heapifyPop(x)


    #Solo se considera cuando el valor es menor al presente en el heap
    def cambioValor(self,posicion,valor):
        self.heap[posicion][1] = valor
        self.heapify(posicion)


def Dijkstra(inicio,tabla,vertices):
    tabla[inicio][1] = 0
    tabla[inicio][2] = True
    tabla[inicio][3] = True
    cola = colaPrioridad()
    for x in vertices[inicio]:
        cola.inserta(x[0],x[1])
        tabla[x[0]][1] = x[1]
        tabla[x[0]][0] = inicio
        tabla[x[0]][2] = True
    #cola.minHeap.imprimeHeap()
    #print(tabla)
    #i = 0
    while not cola.vacio():
        minimo = cola.encuentraMin()
        cola.borraMin()
        tabla[minimo[0]][3] = True
        for x in vertices[minimo[0]]:
            if tabla[x[0]][3] == False:#Es permanente? No, sigue aqui, Si, pasa al siguiente en vertices
                if tabla[x[0]][2] == False:#Es false que ya haya visitado?
                    tabla[x[0]][0] = minimo[0]
                    tabla[x[0]][1] = minimo[1] + x[1]
                    tabla[x[0]][2] = True
                    cola.inserta(x[0],minimo[1] + x[1])
                else:#Es True que ya haya sido visitado
                    if tabla[x[0]][1] > minimo[1] + x[1]:
                        cola.decrementaLlave(x[0],minimo[1] + x[1])
                        tabla[x[0]][1] = minimo[1] + x[1]
                        tabla[x[0]][0] = minimo[0]
        #i = i + 1
    #print(tabla)
    return tabla

def auxiliarSalida(tabla):
    temp_diccionario = {}
    for i in tabla.keys():
        temp_diccionario[i]=tabla[i][1]
    for j in tabla.keys():
        padre = tabla[j][0]
        if padre != '':
            tabla[j][1] = tabla[j][1] - temp_diccionario[padre]


def salida(tabla):
    auxiliarSalida(tabla)
    if not os.path.isfile('salida.txt'):#si no existe, crealo
        f = open("salida.txt","x")
    else:#existe, borra su informacion
        f = open("salida.txt","w")
        f.close()
    f = open("salida.txt","w")
    salida = ""
    contador = 0
    for i in tabla.keys():
        if contador == 0:
            salida = i
        else:
            salida = salida + "," + i
        contador = contador + 1
    salida = salida + "\n"
    for j in tabla.keys(): #se agrega nodo, padre y valor [key,padre,valor] j,tabla[j][0],tabla[j][1]
        if tabla[j][0] != '':#para el nodo principal o nodos desconectados, para que no aparezcan en el resultado final
            salida = salida + j + "," + tabla[j][0] + "," + str(tabla[j][1]) + "\n"
    f.write(salida)
    f.close()

def main():
    f = open(sys.argv[1],"r")
    linea = f.readlines()
    vertices = {}
    tabla = {}
    if linea == []:
        salida(tabla)
        return
    numero = ""
    contador_inicio = 0
    inicio = ""
    i = 0
    while i < len(linea[0]):
        if linea[0][i] == ',' or linea[0][i] == ' ' or linea[0][i] == '\n':
            if contador_inicio == 0:
                inicio  = numero
            vertices[numero] = []
            tabla[numero] = ['',sys.maxsize,False,False]
            numero = ""
            i = i+1
            contador_inicio = contador_inicio + 1
        else:
            numero = numero + linea[0][i]
            i = i + 1
    #print(tabla)
    for i in range(1,len(linea)):
        temp = linea[i]
        j = 0
        valor1 = ""
        valor2 = ""
        valor3 = ""
        while temp[j] != ',':
            valor1 = valor1 + temp[j]
            j = j + 1
        j = j + 1
        while temp[j] != ',':
            valor2 = valor2 + temp[j]
            j = j + 1
        j = j + 1
        while temp[j] != '\n':
            valor3 = valor3 + temp[j]
            j = j + 1
        #Agregamos al diccionario
        valor3 = int(valor3)
        vertices[valor1].append([valor2,valor3])
        vertices[valor2].append([valor1,valor3])
    #print(vertices)
    f.close()
    salida(Dijkstra(inicio,tabla,vertices))
    #print(tabla)
    #print(inicio)
    #salida(tabla)

if __name__ == '__main__':
    main()
    #print(sys.maxsize)
