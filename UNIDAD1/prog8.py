
# a = "hola"
# for i in a:
#     print(ord(i)) #mostrar el ascii del caracter

def validardatos(a):
    c = 0
    c2 = 0
    for i in a:
        if ord(i) >= 97 and ord(i) <= 122:
            c += 1
        if ord(i) >= 48 and ord(i) <= 57:
            c2 += 1
        if c == len(a):
            return True
        elif c2 == len(a): 
            return False
        else:   
            print(a)
            
    
def pedirDatos():
    a = input("Escribe un dato \n")
    if validardatos(a):
        print("Son puras letras")
    else:
        print("Son numeros")


if __name__=='__main__':
    pedirDatos()
