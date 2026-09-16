
# hacer un programa que lea nombre de un producto, fecha de caducidad que solo contendra mes y año y su precio.
# una vez validado los datos el programa mostrara un mensaje indicando si desean otro producto, si es asi vuelve a hacer
# el mismo proceso de lo contrario mostrara el total de los precios, la cantidad de productos y el total con IVA

from validacionesprog12 import validaciones #trae la clase validacioens al archivo validacionesprog12


class principal():
    def __init__(self):
        self.val = validaciones()
      
        self.tp = 0.0  #total de precio
        self.cp = 0    # cantidad de productos

    def incio(self):
   
        while True:
            self.nombreproducto = input("Escribe el nombre del producto \n")
            if self.val.NombreProducto(self.nombreproducto):
                break
            else:
                print("Nombre inválido, intenta de nuevo")

   
        while True:
            self.fechacaducidad = input("Escribe la fecha de caducidad (MM/AAAA) \n")
            if self.val.FechaCaducidad(self.fechacaducidad):
                break
            else:
                print("Fecha inválida, intenta de nuevo")

    
        while True:
            self.precio = input("Escribe el precio del producto \n")
            if self.val.Precio(self.precio):
                break
            else:
                print("Precio inválido, intenta de nuevo")

        self.tp += float(self.precio) # la suma total de los precios
        self.cp += 1 # el conteo total de productos

    def mostrarResultados(self):
        iva = self.tp * 0.16 # definir iva 
        totconiva = self.tp + iva  # se pone en uso iva

        print(f"Precio total sin IVA: {self.tp}")
        print(f"Cantidad de productos: {self.cp}")
        print(f"Precio total con IVA: {totconiva}")


if __name__ == '__main__':
    app = principal()   
    while True:
        app.incio()
        res = input("¿Deseas otro producto? s/n \n")
        if res == "n" or res == "N":
            break
    app.mostrarResultados()