#Crie um programa que recebe os dois lados menores de um triângulo retângulo e uma
#função retorna o valor da hipotenusa.

def hipo(c1,c2) :
    result = (c1 ** 2) + (c2 ** 2) ** (1/2)
    print(result)

c1 = int(input("Digite o valor do cateto 1:"))
c2 = int(input("Digite o valor do cateto 2:"))

hipo(c1, c2)

