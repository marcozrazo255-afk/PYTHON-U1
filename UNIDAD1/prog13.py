# hacer un prorgrama, que lea nombre, apellido materno, apellido paterno dentro de una variable, a continuación, pedira correo
# electronico y telefono de la persona.
# estos datos deben de estar previamente validados de lo contrario se volveran a pedir.
# las validaciones son las siguientes: 
# 1- Solo puede tener 1 nombre y sus apellidos 
# 2- Cada elemento del nombre debe de comenzar con mayuscula
# 3- El correo electronico permite cualquier tipo de caracter, pero obligatoriamente debe de llevar el simbolo de @ y terminar con .com
# 4- El telefono son unicamente numeros y obligatoriamente 10 digitos 

from validacionesprog13 import Validaciones


class principal():
    def __init__(self):
        self.val = Validaciones()
        

    def inicio(self):
        
        while True:
            self.nomcompleto = input("Escribe el nombre, que contenga 1 nombre y sus 2 apellidos: \n")
            if self.val.Nombre(self.nomcompleto):
                break
        while True:
            self.correo = input("Escribe un correo electronico: \n") 
            if self.val.Correo(self.correo):
                break   
        while True:
            self.telefono = input("Escribe un numero de telefono: \n")
            if self.val.NumTelefonico(self.telefono):
               break
    def mostrarDatos(self):                         
        print(f"Nombre: {self.nomcompleto}")
        print(f"Correo: {self.correo}")
        print(f"Teléfono: {self.telefono}")
        


if __name__ == '__main__':
    app = principal()
    app.inicio()
    app.mostrarDatos()
    