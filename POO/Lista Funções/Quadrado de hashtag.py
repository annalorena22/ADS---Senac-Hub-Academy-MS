# Faça um programa que peça um número inteiro positivo ‘n’ ao usuário e imprima um
# quadrado de lado ‘n’ preenchido com hashtags.

def numero(n):
    if n <= 0 :
        print("O número deve ser maior que zero.")

n = int(input("Digite um número:"))
numero(n)

def hashtag(n):
    result = ("#" * n + "\n") * n
    print(result)
hashtag(n)