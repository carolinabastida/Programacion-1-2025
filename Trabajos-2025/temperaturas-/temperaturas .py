#Declaro variable para almacenar los grados Celsius
#asigno un espacio en memoria para guardar los grados celsius
#input palabra reservada que sirve para capturar lo que ingresa el usuario en la pantalla, y float es para almacenar un valor decimal.
celsius= float(input("Ingrese la temperatura en grados Celsius: ")) 

#Realizo calculo
fahrenheir= (celsius * 9/5) + 32

#Realizo calculo
kelvin= celsius + 273.15

#print lo que desea mostrar el programador al usuario, significa imprimir en pantalla
print("RESULTADOS---")
print("Temperatura en Celsius: ", celsius)
print("Temperatura en Fahrenheir:", fahrenheir)
print("Temperatura en Kelvin:", kelvin)
print("---fin del script python---")
