# Programe um software que recebe três números e cria duas funções: uma que retorna o
# maior número e outra que retorna o menor número

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número.:"))

def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3 :
        print("O primeiro número é o maior.")
    elif n2 > n1 and n2 > n3:
        print("O segundo número é o maior.")
    else :
        print("O terceiro número é o maior.")
    
def menor(n1, n2, n3) :
    if n1 < n2 and n1 < n3 :
        print("O primeiro número é o menor.")
    elif n2 < n1 and n2 < n3:
        print("O segundo número é o menor.")
    else :
        print("O terceiro número é o menor.")
maior(n1, n2, n3)
menor(n1, n2, n3)