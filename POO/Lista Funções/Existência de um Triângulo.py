#Crie um programa que recebe os três lados de um triângulo e passa esses valores para uma
# função que verifica se esse triângulo existe ou não. Para que um triângulo exista, cada lado
# deve ser maior que o módulo da subtração dos outros dois lados e menor que a soma dos
# outros dois lados.

def triangulo(l1, l2, l3) :
    if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2) and (l1 > l2 - l3) and (l2 > l1 - l3) and (l3 > l1 - l2):
        print("O triângulo existe.")
    else :
        print("O triângulo não existe.")

l1 = int(input("Digite o valor do lado 1:"))
l2 = int(input("Digite o valor do lado 2:"))
l3 = int(input("Digite o valor do lado 3:"))

while l1 <= 0 or l2 <= 0 or l3 <= 0 :
    print("Os valores devem ser maior que zero.")
    l1 = int(input("Digite o valor do lado 1:"))
    l2 = int(input("Digite o valor do lado 2:"))
    l3 = int(input("Digite o valor do lado 3:"))
else: 
    triangulo(l1,l2,l3)
