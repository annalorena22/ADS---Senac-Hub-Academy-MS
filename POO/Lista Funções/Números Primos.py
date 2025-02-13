# Faça um programa que verifica se um número é primo. Um número é primo se ele não
# possui divisores além de 1 e ele mesmo.

n = int(input("Digite o número para verificar se é primo ou não: "))

def n_primo(n):
  if(( n%2 != 0) and (n%1 and n%n) == 0) or n == 2:
    print("O número é primo!")
  else:
    print("O número não é primo!")

n_primo(n)