import sys

def validarNumerosEnteros(x):
    a = 0
    try:
        a = int(x)
        return True
    except ValueError:
        print("No son numeros Enteros")
        return False 
def validarNumerosDecimales(x):
    a = 0
    try:
        a = float(x) 
    except ValueError:
        print("No son numeros Decimales")
        return False 

def validarletras(x):
    if x.isupper(): 
        print("Son mayusculas")
        return True 
    elif x.islower(): 
        print("Son minusculas")
        return True
    else:
        return False

def inicio():
    a = input("Escribe un dato: \n")
    if validarletras(a):
        print("Son letras")
    elif validarNumerosEnteros(a):
        print("Son numeros sin decimales")
    elif validarNumerosDecimales(a):
        print("Son numeros con decimales")
    else:
        print("Son tipo de datos distintos a los ateriores ")
        sys.exit()




if __name__=='__main__':
    inicio()