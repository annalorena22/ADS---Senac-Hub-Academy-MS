frutas = ["tangerina", "limao", "abacate", "banana"]
 
while True:
  try:
      resposta = int(input("- Digite um número para visualizar um elemento da lista :"))
      print("-", frutas[resposta])
      break
  except IndexError:
      print("- Essa posição não existe na lista :(")