# Um número é dito ser perfeito quando ele é igual à soma de seus divisores. Por exemplo, o
# seis é perfeito, pois: 6=1+2+3.
# Crie um programa que pede um número ao usuário e diga se ele é perfeito ou não.

n = int(input("Digite o primeiro número:"))

def perfeito(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    if divisors_sum == n:
        print("É um número perfeito.")
    else:
        print("Não é um número perfeito.")
perfeito(n)
