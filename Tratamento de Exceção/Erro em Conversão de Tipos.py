while True:
    a = input("Digite um número:")
    try :
        a = int(a)
        break
    except ValueError :
        print("Por favor digite um número")
   
print(a)