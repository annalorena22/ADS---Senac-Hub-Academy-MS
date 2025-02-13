# Escreva uma função que recebe uma string e conta quantas vogais (a, e, i, o, u) ela contém.
palavra = input("Digite uma palavra para a contagem de vogais: ")
def vogal(palavra):
  lista = []
  vogais = ["a","e","i","o","u"]
  for i in palavra:
    if i in vogais:
      lista.append(i)
  for i in vogais:
    contagem = lista.count(i)
    print(f"O número de {i} é de {contagem}")
vogal(palavra)