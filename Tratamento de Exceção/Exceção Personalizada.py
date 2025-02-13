class Botao01(Exception):
    pass
 
class Botao02(Botao01):
    pass
 
class Botao03(Botao02):
    pass
 
for cls in [Botao01, Botao02, Botao03]:
    try:
        raise cls(Botao01)  
    except Botao03:
        print("Botão03")
    except Botao02:
        print("Botão02")
    except Botao01:
        print("Botão01")