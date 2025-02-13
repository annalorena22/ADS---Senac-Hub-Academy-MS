class Habilitacao:
    def __init__(self, tipo=None, descricao=None):
        self.tipo = tipo      
        self.descricao = descricao

    def hab_info(self):
       return f"Tipo da Habilitação: {self.tipo}\nDescrição: {self.descricao}"

class Veiculo(Habilitacao):
    def __init__(self, nome, marca, modelo, ano_fabricacao, capacidade_passageiros, quantidade_eixos, tipo=None, descricao=None):
        super().__init__(tipo, descricao)
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.capacidade_passageiros = capacidade_passageiros
        self.quantidade_eixos = quantidade_eixos
        self.observacao = None
        self.habilitacao_necessaria = None
        self.tracao = None  
        self.especie_veiculo = None
        self.categoria_veiculo = None
            
            
    def __str__(self):
        info = "====================================================================\n"
        info += f"Nome: {self.nome}\n"
        info += f"Marca: {self.marca}\n"
        info += f"Modelo: {self.modelo}\n"
        info += f"Ano de Fabricação: {self.ano_fabricacao}\n"
        info += f"Capacidade de Passageiros: {self.capacidade_passageiros}\n"
        info += f"Quantidade de Eixos: {self.quantidade_eixos}\n"
        if self.observacao:
            info += f"Observação: {self.observacao}\n"
        
        if self.habilitacao_necessaria:
            info += self.habilitacao_necessaria.hab_info() + "\n"
        else:
            info += "Não é necessária Carteira Nacional de Habilitação.\n"

        if self.tracao:
            info += f"Tipo de Tração: {self.tracao}\n"

        if self.especie_veiculo:
            info += f"Espécie do Veículo: {self.especie_veiculo}\n"

        if self.categoria_veiculo:
            info += f"Categoria do Veículo: {self.categoria_veiculo}\n"
        return info