# Faça um programa que verifica se uma palavra ou frase é um palíndromo. Um palíndromo é
# uma palavra ou frase que se lê da mesma forma de trás para frente. Por exemplo, “arara” é
# um palíndromo.

def palindromo(palavra):
  lista = []
  for i in palavra:
    lista.append(i)
  lista.reverse()
  reverso = ""
  for i in lista:
    reverso += i

  if palavra == reverso:
    print("É um palindromo!")
  else:
    print("Não é um palindromo!")


palavra = input("Digite a palavra que deseja saber se é um palindromo: ")
palindromo(palavra)