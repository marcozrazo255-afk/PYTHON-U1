# hacer un programa que pida una cantidad en pesos (numeros con decimales)el programa validara que sea un numero correcto 
# y si el dato es correcto, calculara y mostrara su equivalente en dolares y euros, si el numero es incorrecto se volvera
# a pedir.
# el programa no termina hasta que muestre en pantalla los resultados solicitados 


import sys

def validarNumeros(a):
    i = a.find('.')
    if i == -1:
        return False
    else:
        try:
            v = float(a)
            return True
        except ValueError:
            return False

        


def inicio():
    al = 0.0
    cd = 0.0
    ce = 0.0
    while(True):
        a = input("Escribe una cantidad en pesos (Con decimales)\n")
        if validarNumeros(a):
            al = float(a)
            cd = al / 16.95
            print(f"la conversion a dolares es: {cd}")
            ce = al / 19.67
            print(f"la conversion a euros es: {ce}")
            break
        else:
            print("Error valor incorrecto")



if __name__=='__main__':
    inicio()

