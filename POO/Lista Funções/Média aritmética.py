# Crie um programa que pede ao usuário para digitar uma sequência de números e, em
# seguida, calcula a média aritmética desses números.

lista = []
def media(num):
  tamanho = len(lista)
  soma = sum(lista)
  resultado = soma/tamanho
  print(f"A média dos números digitados é igual a {resultado}")

qtd_dig = int(input("Digite quantos números deseja digitar: "))

for i in range(qtd_dig):
  num = int(input("Digite aqui: "))
  lista.append(num)
media(num)  