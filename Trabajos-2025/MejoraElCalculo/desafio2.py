valores= input("Ingrese las notas separadas por comas: ")# 2,4,  8 

#recorremos valores, cada nota separa por la coma la cargamos en la variable nota. con strip le eliminamos los espacios en blancos.
calificaciones= [int(nota.strip()) for nota in valores.split(",")] # 2,4,8  ->  [2,4,8]

# sum en este caso haria 2+4+8, suma los valores que se encuentran dentro de la lista
promedio= sum(calificaciones) / len(calificaciones) # len -> largo de la lista

print ("El promedio es: ", promedio)

