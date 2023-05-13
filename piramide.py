bloques = int(input("Introduzca el número de bloques disponibles: "))
 
altura = 0
utilizados = 0
restantes= 0 
por_fila = 1
 
while restantes > piso_siguiente:
    altura=altura + 1
    if por_fila== 0:
        por_fila = 1
    else:
        por_fila=por_fila + altura
        utilizados= bloques - por_fila
        
#codigo encontrado en internet
bloques = int(input("Introduzca el número de bloques disponibles: "))
 
altura = 0
 
utilizados = 0
por_fila = 1
 
while True:
    utilizados += por_fila
    if utilizados > bloques:
        break
 
    altura += 1
    por_fila += 1
 
 
print("La altura de la pirámide es de: ", altura)
