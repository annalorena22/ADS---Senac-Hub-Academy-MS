# Escreva uma função que recebe um número inteiro e retorna a soma de seus dígitos. Por
# exemplo, se o número for 123, a função deve retornar 6 (1 + 2 + 3).

def soma(num):
  soma = 0
  for i in num:
    soma += int(i)
  print("A soma dos digitos é igual a %i" % soma)

num = input("Digite o número que deseja somar os digitos: ")
soma(num)