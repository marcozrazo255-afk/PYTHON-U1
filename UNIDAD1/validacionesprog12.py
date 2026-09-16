

# clase que agrupa todas las validaciones
class validaciones():

        # validacion que contiene 
    def NombreProducto(self, a):
       
        c = 0 # Contador de letras minúsculas y espacios
        c2 = 0 # Contador de letras mayúsculas
        for i in a:
            if (ord(i) >= 97 and ord(i) <= 122) or ord(i) == 32:
                c += 1
            if ord(i) >= 65 and ord(i) <= 90:
                c2 += 1
        if c == len(a):
            return True
        elif c2 == len(a): 
            return False
        else:   
            print(a)

   # validación que verifica que la fecha tenga formato MM/AAAA
    def FechaCaducidad(self, a):
        i = a.find('/')
        if i == -1: # verifica que exista un slash
            return False
        if i != 2: # verifica que el slash esté en la posición 2
            return False
        if len(a) != 7: # verifica que la cadena tenga 7 caracteres (2 + / + 4)
            return False
        
        c = 0 #contador de digitos 
        c2 = 0 #contador de slash 
        

        for sh in a:
            # numeros ascci del 0-9
            if ord(sh) >= 48 and ord(sh) <= 57:
                c += 1
            if sh == '/':
                c2 += 1
            if c2 == 1 and c == 6:
                return True
            elif c2 > 1:
                return False
            
      # validación que verifica que el precio sea un número con punto decimal
    def Precio(self, a):
        i = a.find('.')
        if i == -1: # verifica que exista un punto
            return False
        else:
            # esta linea intenta hacer el float, si es correcto retorna true, y si sucede un error valueError atrapa ese error y retorna
            # falso
            try: 
                v = float(a)    
                return True
            except ValueError:
                return False