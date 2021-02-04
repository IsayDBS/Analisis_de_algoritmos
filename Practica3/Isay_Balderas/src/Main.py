import math

def shellSort(A,n):
    h = int(n/2)
    while h>0:
        print("h = " + str(h))
        for i in range(h,n):
            v = A[i]
            j = i
            #print(A)
            while j >= h and A[j-h] > v:
                A[j] = A[j-h]
                j = j - h
            A[j] = v
            print(A)
        h = int(h/2)

def Hibbard(A,n):
    k = int(math.log(n,2))
    h = int((2 ** k) - 1)
    while h>0:
        print("h = " + str(h))
        for i in range(h,n):
            v = A[i]
            j = i
            #print(A)
            while j >= h and A[j-h] > v:
                A[j] = A[j-h]
                j = j - h
            A[j] = v
            #print(A)
            print(A)
        k = k - 1
        h = int((2 ** k)-1)

def menu(A):
    ciclo = True
    while ciclo == True:
        print("Tu arreglo es: " + str(A))
        print()
        print("Elige una modificacion de shell sort")
        print()
        print("0.Salir")
        print()
        print("1.ShellSort normal")
        print()
        print("2.ShellSort Hibbard")
        print()
        try:
            valor = int(input())
            if valor == 0:
                ciclo = False
            elif valor == 1:
                shellSort(A,len(A))
                ciclo = False
            elif valor == 2:
                Hibbard(A,len(A))
                ciclo = False
            else:
                print("Opcion no valida")
        except:
            print("Valor no valido")

def main():
    f = open("elementos.txt","r")
    A = []
    linea = f.readline()
    i = 0
    largo = len(linea)
    acumulador = ""
    while i < largo:
        if linea[i] != ',' and linea[i] != '\n':
            acumulador = linea[i]
            i = i + 1
            while linea[i] != ',' and linea[i] != '\n':
                acumulador = acumulador + linea[i]
                i = i + 1
            A.append(int(acumulador))
            acumulador = ""
        i = i + 1
    f.close()
    menu(A)

main()
