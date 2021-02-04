El siguiente codigo funciona como sigue:
python3 Main.py grafica.txt
Es importante notar que el archivo grafica.txt necesita un salto de linea en el ultimo renglon, si no, el programa falla (probado en windows donde no hay salto de linea y el programa falla, este codigo fue probada en ubuntu con python 3.8.9, donde al guardar el archivo grafica.txt se da un salto de linea siempre al final, desconozco la razon de esta diferencia entre sistemas operativos).
En la entrada, es considerada que la grafica no es digrafica, es decir, (vertice,vertice,distancia) es una arista que conecta ambas vertices y puede ir en ambos lados, no es digrafica. 
Si no hay archivo salida.txt, se crea; en caso de que exista, se borra su contenido y se actualiza.
En salida.txt, la primer linea son los vertices, las siguiente aparecen las aristas de la forma (vertice,vertice,peso)
