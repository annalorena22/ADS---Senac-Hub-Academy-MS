class Divisao():
    def __init__(self):
        pass
   
    def Dividir(self, n1, n2):
#        return numero1/numero2
        try:
            n1 = int(n1)
            n2 = int(n2)
            return n1/n2           
        except ZeroDivisionError:
            print("Tentativa de dividir por zero")
        except ValueError:
            print("ValueError")
 
n1 = input()
n2 = input()    
 
novadivisao = Divisao()
print(novadivisao.Dividir(n1,n2))