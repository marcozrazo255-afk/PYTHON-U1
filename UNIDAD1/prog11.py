from validacionesprog11 import validaciones


class Programa():
    def __init__(self):
        self.val = validaciones()
        
        
    def PedirDatos(self):
        self.nombre = input("Escribe el nombre \n")
        self.edad = input("Escribe la edad \n")
        self.estatura = input("Escribe la estatura de la persona \n")
        if self.val.ValidarLetras(self.nombre):
            print("El nombre es correcto..")
        else:
            print("El nombre no es correcto")
        if self.val.ValidarNumeros(self.edad):
            print("La edad es correcta..")
        else:
            print("La edad no es correcta")
        if self.val.ValidarNumerosConDecimales(self.estatura):
            print("La altura es correcta..")
        else:
            print("La altura no es correcta")


                                                                                                                                                                                                                                                                                                                                            
if __name__=='__main__':
    while(True):
        app = Programa()
        app.PedirDatos()
        res = input("Deseas intentar otra vez s/n\n")
        if res == "N" or res == "n":
            break