Programa probado en Ubuntu 20.10 con Python 3.8.6
Las librerias usadas son csv y sys.
Se pueden recibir a los mas 2 argumentos de la linea de comandos, se considera que siempre estos valores de entrada seran numeros, donde el segundo es a lo mas int(n/2).
Si solo recibe un argumento, entonces procede a generar el experimento 1, donde se devolvera un archivo resultado.csv, cada vez que se corre el primer experimento, se sobreescribe este documento

Los saltos son de un nodo al otro, es decir, pongamos el ejemplo [4,5,6,7,8,9,1,2,3,10,11,12]

Ingresar a una lista vacia cuenta como un salto, al ingresar el nodo 4, se revisa si esta a la derecha o izquierda del ultimo nodo, en este caso 4, por lo que aqui tambien se suma un salto, avanzando en el nodo 1, que el ultimo agregado fue 9, saltara al 9,8,7,6,5 y 4, haciendolo 6 saltos.
Aclaro esto porque en los ejemplos proporcionados en los casos de 12 si salen iguales, pero en otros no, como por ejemplo n = 13 y d = 6, donde hace 14 koe's, porque salta a los nodos 6 y 7.

Linea de Comando estandar: python3 Main.py 10 5

Linea de Comando Experimento 1: python3 Main.py 10

Cualquier otra cosa, se envia un mensaje que dice "Faltan o se reciben muchos argumentos"
