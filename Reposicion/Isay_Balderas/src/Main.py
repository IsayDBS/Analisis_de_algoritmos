import sys
import csv

class DoublyLinkedList():

    def __init__(self,valor,izquierdo,derecho):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho

def conectaIzq(root,node):
    if root.izquierdo == None: #primero de la lista
        node.derecho = root
        root.izquierdo = node
    else:
        root.izquierdo.derecho = node
        node.izquierdo = root.izquierdo
        root.izquierdo = node
        node.derecho = root

def conectaDer(root,node):
    if root.derecho == None: #ultimo de la lista
        node.izquierdo = root
        root.derecho = node
    else:
        root.derecho.izquierdo = node
        node.derecho = root.derecho
        root.derecho = node
        node.izquierdo = root

def inserta(root,node,koe):
    if node.valor < root.valor:
        while root.izquierdo != None:
            koe[0] = koe[0] + 1#suma a koe
            #print(str(koe[0]) + " del vertice " + str(node.valor))
            if root.izquierdo.valor <= node.valor:
                conectaIzq(root,node)
                return node
            root = root.izquierdo
        conectaIzq(root,node)
    else: #node.valor >= root.valor
        while root.derecho != None:
            koe[0] = koe[0] + 1 #suma a koe
            #print(str(koe[0]) + " del vertice " + str(node.valor))
            if root.derecho.valor >= node.valor:
                conectaDer(root,node)
                return node
            root = root.derecho
        conectaDer(root,node)
    koe[0] = koe[0] + 1
    #print(str(koe[0]) + " del vertice " + str(node.valor))
    return node

def localInsertionSort(x):
    if x == []:
        return
    root = DoublyLinkedList(x[0],None,None)
    i = 1
    ultimo = len(x)
    koe = [1]
    while i < ultimo:
        auxiliar = DoublyLinkedList(x[i],None,None)
        root = inserta(root,auxiliar,koe)
        i = i + 1
        #print("root" + str(root.valor))
    print(imprimeLista(root))
    print()
    print("koe: " + str(koe[0]))

def localInsertionSortExp1(x):
    if x == []:
        return
    root = DoublyLinkedList(x[0],None,None)
    i = 1
    ultimo = len(x)
    koe = [1]
    while i < ultimo:
        auxiliar = DoublyLinkedList(x[i],None,None)
        root = inserta(root,auxiliar,koe)
        i = i + 1
    return(koe[0])

def imprimeLista(node):
    while node.izquierdo != None:
        node = node.izquierdo
    salida = "[" + str(node.valor)
    node = node.derecho
    while node != None:
        salida = salida + ", " +str(node.valor)
        node = node.derecho
    return salida + "]"

def swap(x,pos1,pos2):
    x[pos1],x[pos2] = x[pos2],x[pos1]

def agarra(i,n):
    lista = []
    while i <= n:
        lista.append(i)
        i = i + 1
    return lista

def generaLista(n,d):
    lista = []
    i = 1
    posicionb = -2
    posicionB = -1
    while i <= n:
        if i + d > n:
            lista.insert(0,agarra(i,n))
            break
        #agarramos de derecha a izquierda
        lista.insert(posicionB,agarra(n-d+1,n))
        n = n - d
        posicionB = posicionB - 2
        #agarramos de izquierda a derecha
        lista.insert(posicionb,agarra(i,i + d - 1))
        posicionb = posicionb - 2
        i = i + d
    #hasta aqui, lista es una lista de sublistas en estilo zig zag
    resultado = [] #lista solo con los numeros en forma de zig zag
    for l in lista:
        resultado = resultado + l
    #print(resultado)
    return resultado

def imprimirTabla(n):
    mitad = int(n/2)
    generar = []
    listas = []
    if n < 20:#de 1 hasta n/2
        for i in range(1,mitad+1):
            generar.append(i)
            auxiliar = generaLista(n,i)
            listas.append(auxiliar)
    elif n >= 20 and n < 100:#1,2,5,10,15,20,30,50
        posibles = [1,2,5,10,15,20,30,50]
        for i in posibles:
            if i <= int(n/2):
                generar.append(i)
                auxiliar = generaLista(n,i)
                listas.append(auxiliar)
    else:#10,20,50,100,200,500,1000
        posibles = [10,20,50,100,200,500,1000]
        for i in posibles:
            if i <= int(n/2):
                generar.append(i)
                auxiliar = generaLista(n,i)
                listas.append(auxiliar)
    koes = ["koe"]
    for i in range(0,len(generar)):
        koes.append(localInsertionSortExp1(listas[i]))
    generar.insert(0,"")
    with open('resultado.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(generar)
        writer.writerow(koes)

def main():
    if len(sys.argv) == 2:
        imprimirTabla(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        lista = generaLista(int(sys.argv[1]),int(sys.argv[2]))
        print("Lista zigzag:")
        print(lista)
        print()
        print("Lista ordenada:")
        localInsertionSort(lista)
    else:
        print("Faltan o se reciben muchos argumentos")


if __name__ == '__main__':
    main()
