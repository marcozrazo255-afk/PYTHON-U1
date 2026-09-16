#hacer un programa que lea 4 numeros y calcule el promedio 

a = int(input("Ecribe un numero: \n"))
b = int(input("Ecribe un numero: \n"))
c = int(input("Ecribe un numero: \n"))
d = int(input("Ecribe un numero: \n"))

promedio = (a+b+c+d)/4
print(f"El promedio es: {promedio}\n")

if promedio >= 7:
    print("Si aprobo")
else:
    print("No aprobo")
