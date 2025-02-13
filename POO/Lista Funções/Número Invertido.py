# Crie um software que recebe um número do usuário, passa esse valor para uma função e ela
# retorna o número escrito ao inverso. Por exemplo, se o usuário der o valor 1234, a função
# deve retornar 4321. Dica: primeiro, crie uma função que conta quantos dígitos tem um
# número.

n = input("Digite um número:")
lista = []
def inverter(n):
    for i in n:
        lista.append(i)
    lista.reverse()
    n_inverso = ""
    for i in lista:
        n_inverso += i
    print(n_inverso)
inverter(n)