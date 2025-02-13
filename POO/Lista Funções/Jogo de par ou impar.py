# Escolha 0 para par ou 1 para ímpar. Em seguida, forneça um número. Crie um programa que
# determine se a soma do número escolhido com um número aleatório é par ou ímpar.

import random
def par_impar(num):
  valor = random.randint(1,2) + num
  if valor % 2 == 0:
    print("par ganhou!")
  else:
    print("ímpar ganhou!")

num = int(input("Digite 0 para par ou 1 para ímpar: "))
while num != 0 and num != 1:
    num = int(input("Voce deve digitar 0 para par ou 1 para ímpar: "))

par_impar(num)
