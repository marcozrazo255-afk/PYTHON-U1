

class validaciones():
    def ValidarLetras(self, a):
        c = 0
        c2 = 0
        
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
    
    def ValidarNumeros(self, a):
       a = 0
       try:
            a = int(a)
            return True
       except ValueError:
            print("No son numeros Enteros")
            return False 

    def ValidarNumerosConDecimales(self, a):
        a = 0
        try:
            a = int(a)
            return True
        except ValueError:
            print("No son numeros Enteros")
            return False 


