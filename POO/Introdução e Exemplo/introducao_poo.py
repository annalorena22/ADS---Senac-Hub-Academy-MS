class Veículo:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def acelerar(self):
        print(f"O veículo {self.modelo} da marca {self.marca} acelerou!")

    def freiar(self):
        print(f"O veículo {self.modelo} da marca {self.marca} freiou!")

class Carro(Veículo):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)
    def abrirPorta(self):
        print("Abriu a porta.")

class Moto(Veículo):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)
        self.guidao = True

    def cortarGiro(self):
        print("Ram Dam Dam Dam Dammm.")

fusca = Carro("Volkswagen", "Fusca", "Azul", 1975)
harley = Moto("Harley Davidson", "BigBoy", "Bordo", 2019)

print(vars(fusca))

fusca.acelerar()
fusca.freiar()
harley.acelerar()
harley.cortarGiro()