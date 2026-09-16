

class Validaciones():
     def Nombre(self, a):
    # 1. Contar letras y espacios
        c = 0 #contador para letras
        c2 = 0 # contador para mayusculas
        for i in a:
            # validacion de mayuscula, minuscula, y espacio
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90) or ord(i) == 32:
                c += 1

        if c != len(a):
            print("ERROR, el nombre solo puede contener letras y espacios")
            return False

        # 2. Verificar 2 palabras
        partes = a.split()
        if len(partes) != 3:
            print("ERROR, el nombre debe contener 2 palabras")
            return False

        # 3. Verificar mayúsculas iniciales
        for palabra in partes:
            if ord(palabra[0]) >= 65 and ord(palabra[0]) <= 90:
                c2 += 1

        if c2 != len(partes):
            print("ERROR, cada palabra debe empezar con una mayúscula")
            return False

        return True
     # validacion de correo
     def Correo(self, correo):
        nc = correo[len(correo)-4: len(correo)]
        if nc == ".com":
            return True
        else:
            print("El correo debe terminar con .com")
            return False
    # validacion de numero
     def NumTelefonico(self, telefono):
        if len(telefono) != 10:
            print("El teléfono debe tener 10 dígitos")
            return False

        try:
            t = int(telefono)
            return True
        except ValueError:
            print("El teléfono debe contener solo números")
            return False















# def NombreCompleto(self, a):
       
#         c = 0 
#         c2 = 0 
#         for i in a:
#             if (ord(i) >= 97 and ord(i) <= 122) or ord(i) == 32:
#                 c += 1
#             if ord(i) >= 65 and ord(i) <= 90:
#                 c2 += 1
#         if c == len(a):
#             return True
#         elif c2 == len(a): 
#             return False
#         else:   
#             print(a)

#     def Correo(self, a):
#         pass