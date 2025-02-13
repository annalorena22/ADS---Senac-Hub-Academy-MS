# Crie um programa que recebe um número inteiro positivo ‘n’ e calcula o fatorial desse
# número. O fatorial de ‘n’ é o produto de todos os números inteiros positivos de 1 até ‘n’.
# Por exemplo, 5!=5⋅4⋅3⋅2⋅1=120

def fatorial(n):
  aux = 1
  for i in range(1,n+1):
    resultado = aux * i
    aux = resultado
  print(f"O fatorial de {n} é igual a {resultado}")

n = int(input("Digite um número: "))
fatorial(n)