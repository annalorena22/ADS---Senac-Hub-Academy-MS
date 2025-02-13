produtos = {'Pão': [15],
            'Celular': [10],
            'Papel Higiênico': [100]}
 
print("→ Produtos : Pão, Celular, Papel Higiênico")
while True:
  try:
    x = input("\n- Digite o nome do produto para visualizar seu valor.\n• ")
    print("• Valor :", produtos[x])
    break
  except KeyError:
      print("\n- Esse produto não existe 😕")