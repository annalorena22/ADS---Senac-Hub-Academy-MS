# Criar um sistema de classificação de animais vertebrados usando programação orientada a objetos (POO) em Python, 
# representando subdivisões até chegar a classes específicas como Ornitorrinco, Morcego e Baleia.

# Criação das Classes Principais:

# Inicie com a classe geral Animal que conterá características comuns a todos os animais (ex: nome científico).
# Crie subclasses que representem Vertebrados e, a partir daí, vá subdividindo em classes menores (por exemplo, Mamíferos, Répteis, etc.).
# Características Específicas:

# Cada classe deve conter atributos e métodos específicos de cada subdivisão. Por exemplo:
# Mamíferos: método amamentar().
# Aves: método voar().
# Chegue até as classes mais específicas: Ornitorrinco, Morcego e Baleia.
# Atributos e Métodos:

# Atributos como esqueleto, habitat e alimentacao devem ser herdados pelas subclasses.
# Métodos devem ser implementados para ações comuns (ex: seMovimentar()) e específicas (ex: botarOvo() para algumas classes). 

class Animal:
    def __init__(self, nome_popular, nome_cientifico):
        self.nome_popular = nome_popular
        self.nome_cientifico = nome_cientifico
        print("=============================================================================================\n")
        print(f"Nome: {self.nome_popular}\nNome Científico: {self.nome_cientifico}\n")
    def seMovimentar(self):
        print(f"{self.nome_popular} se movimentou.\n")

class Vertebrados(Animal):
    def __init__(self, nome_popular, nome_cientifico):
        super().__init__(nome_popular, nome_cientifico)
        print(f"{self.nome_popular} é Vertebrado.\n")
    def mostrarColuna(self):
        print(f"Olha, eu sou {self.nome_popular} e tenho coluna vertebral!\n")

class Aves(Vertebrados):
    def __init__(self, nome_popular, nome_cientifico):
        super().__init__(nome_popular, nome_cientifico)
        print(f"{self.nome_popular} é da Classe Aves.\n")
    
    def voar(self):
        print(f"{self.nome_popular} voou.\n")

class Repteis(Vertebrados):
    def __init__(self, nome_popular, nome_cientifico):
        super().__init__(nome_popular, nome_cientifico)
        print(f"{self.nome_popular} é da Classe Répteis.\n")
    
    def botarOvo(self):
        print(f"{self.nome_popular} botou um ovo.\n")

class Anfibios(Vertebrados):
    def __init__(self, nome_popular, nome_cientifico):
        super().__init__(nome_popular, nome_cientifico)
        print(f"{self.nome_popular} é da Classe Anfíbios.\n")
    
    def pular(self):
        print(f"{self.nome_popular} pulou na lagoa.\n")

class Peixes(Vertebrados):
    def __init__(self, nome_popular, nome_cientifico):
        super().__init__(nome_popular, nome_cientifico)
        print(f"{self.nome_popular} é da Classe Peixes.\n")
    
    def nadar(self):
        print(f"{self.nome_popular} continuou a nadar.\n")

class Mamiferos(Vertebrados):
    def __init__(self, nome_popular, nome_cientifico):
        super().__init__(nome_popular, nome_cientifico)
        print(f"{self.nome_popular} é da Classe Mamífero.\n")
    def amamentar(self):
       print(f"{self.nome_popular} amamentou seu filhote.\n")
    def botarOvo(self):
        print(f"{self.nome_popular} botou um ovo porque tem mamífero que bota ovo.\n")

class Ornitorrinco(Mamiferos):
    def __init__(self, nome_popular, nome_cientifico):
        super().__init__(nome_popular, nome_cientifico)
        print("Sou um ornitorrinco.\n")
    def amamentar(self):
        print("Meus filhotes estão lambendo o suor da minha barriguinha.\n")

class Morcego(Mamiferos):
    def __init__(self, nome_popular, nome_cientifico):
        super().__init__(nome_popular, nome_cientifico)
        print("Sou um morcego.\n")
    
    def morderPescoco(self):
        print(f"{self.nome_popular} mordeu seu pescoço, chama o samu.\n")

class Baleia(Mamiferos):
    def __init__(self, nome_popular, nome_cientifico):
        super().__init__(nome_popular, nome_cientifico)
        print("Sou uma baleia.\n")
    
    def nadar(self):
        print(f"{self.nome_popular} está nadando no oceano.\n")