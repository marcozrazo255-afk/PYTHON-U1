#hacer un programa que lea 1 numero correspondinte de 1 y 9, a continuacion realizara una pregunta
#indicando si desea introducir otro numero, si la respuesta es si, realizara nuevamente la entrada
#de datos, si la respuesta es no el programa mostrara la suma, promedio y cantidad de numeros
#introducidos, ademas de los numeros que se introdujeron 

c = 0 #contador 
p = "s"
suma = 0
su = ""
while(p=="s"):
    a = int(input("Escribe un numero: \n")) #preguntar el numero
    if a >= 1 and a <= 9:                                        #Verificar que se encuentra en el rango 1-9
        c += 1 #contabilizar los numeros
        suma += a
        su += str(a)
        su += ","
        p = input("deseas agregar otro  nuemro s/n \n" )  #preguntar si desea otro numero
        if p == "s" or p == "S":
            print("Se introducira otro numero")
        else:
            break
    else:
        print("Escribe un numero entre el 1-9 \n vulve a intentarlo:")

print(f"la suma de los numeros son: {suma} y el promedio es {suma/c} y la cantidad de numeros son {c} y los numeros son {su}")
    



