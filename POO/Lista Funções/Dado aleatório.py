# Crie um dado em C++. A função deve sortear um número aleatório de 1 até 6. Agora, faça
# com que o dado seja lançado 100 vezes, mil vezes e 1 milhão de vezes. Armazene o valor
# que ele forneceu em cada lançamento e mostre quantas vezes cada número foi sorteado.
# Compare os resultados com a estatística.

import random
jogar = int(input("Digite quantas vezes deseja jogar o dado: "))
def dado(jogar):
  lista = []
  n = 1
  for i in range(jogar):
    valor = random.randint(1,6)
    lista.append(valor)

  for i in range(0,6):
    cont = lista.count(n)
    print(f"O número{n} foi sorteado {cont} vezes")
    n += 1

dado(jogar)