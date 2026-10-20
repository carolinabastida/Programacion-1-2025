num= int(input("Ingrese un numero entero"))
num2=num-1

while num2>0:
  num= num * num2
  num2 = num2-1

print("Factorial: ", num )