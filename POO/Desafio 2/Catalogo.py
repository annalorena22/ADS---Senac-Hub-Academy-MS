from Veiculo import *

habilitacao_A = Habilitacao("A", "Motocicletas")
habilitacao_B = Habilitacao("B", "Categoria para veículos de 4 rodas (carros) com peso total de 35,5 toneladas.")
habilitacao_C = Habilitacao("C", "Categoria para veículos de transporte de carga")
habilitacao_D = Habilitacao("D", "Categoria para veículos de transporte de passageiros")

trator = Veiculo("Trator", "Caterpillar", "D8", 2021, 1, 2)
trator.observacao = "Apenas um trator"
trator.habilitacao_necessaria = habilitacao_C
trator.tracao = "Automotor"
trator.especie_veiculo = "Veículo de tração"
trator.categoria_veiculo = "Particular"
print(trator)

eletrico_competicao = Veiculo("Carro de corrida", "Rimac", "Concept Two", 2022, 1, 4)
eletrico_competicao.observacao = "Corre muito"
eletrico_competicao.habilitacao_necessaria = habilitacao_B
eletrico_competicao.tracao = "Elétrico"
eletrico_competicao.especie_veiculo = "Veículo de competição"
eletrico_competicao.categoria_veiculo = "Particular"
print(eletrico_competicao)

reboque = Veiculo("Reboque", "Trail King", "TK80", 2020, 2, 4)
reboque.observacao = "Para transporte especial"
reboque.habilitacao_necessaria = habilitacao_C
reboque.tracao = "Reboque"
reboque.especie_veiculo = "Veículo especial"
reboque.categoria_veiculo = "Oficial"
print(reboque)

colecao = Veiculo("Versão Colecionador", "Rolls Royce", "Phantom II", 1930, 4, 2)
colecao.observacao = "Carro antigo de luxo"
colecao.habilitacao_necessaria = habilitacao_B
colecao.tracao = "Automotor"
colecao.especie_veiculo = "Veículo de coleção"
colecao.categoria_veiculo = "De representação diplomática"
print(colecao)

carro_autoescola = Veiculo("Carro", "Hyundai", "i20", 2022, 5, 2)
carro_autoescola.observacao = "Carro de carro_autoescola"
carro_autoescola.habilitacao_necessaria = habilitacao_B
carro_autoescola.tracao = "Automotor"
carro_autoescola.especie_veiculo = "Veículo de passageiro"
carro_autoescola.categoria_veiculo = "De aprendizagem"
print(carro_autoescola)

eletrico_carga = Veiculo("Elétrico de Carga", "Nikola", "Tre", 2023, 2, 4)
eletrico_carga.observacao = "Caminhão elétrico"
eletrico_carga.habilitacao_necessaria = habilitacao_C
eletrico_carga.tracao = "Elétrico"
eletrico_carga.especie_veiculo = "Veículo de carga"
eletrico_carga.categoria_veiculo = "Particular"
print(eletrico_carga)

carroca_humana = Veiculo("Riquixá", "Generic", "Model R", 2020, 2, 2)
carroca_humana.observacao = "Carroça puxada por humano"
carroca_humana.tracao = "Propulsão humana"
carroca_humana.especie_veiculo = "Veículo especial"
carroca_humana.categoria_veiculo = "Particular"
print(carroca_humana)

carroca_animal = Veiculo("Carroça", "Boi", "Antiga", 1920, 2, 2)
carroca_animal.observacao = "Carroça histórica"
carroca_animal.habilitacao_necessaria = habilitacao_B
carroca_animal.tracao = "Tração animal"
carroca_animal.especie_veiculo = "Veículo de coleção"
carroca_animal.categoria_veiculo = "Oficial"
print(carroca_animal)

caminhao_carros = Veiculo("Caminhão Trailer", "Featherlite", "Race Trailer", 2021, 2, 4)
caminhao_carros.observacao = "Para transporte de carros de corrida"
caminhao_carros.habilitacao_necessaria = habilitacao_C
caminhao_carros.tracao = "Reboque"
caminhao_carros.especie_veiculo = "Veículo de competição"
caminhao_carros.categoria_veiculo = "De representação diplomática"
print(caminhao_carros)

caminhao_autoescola = Veiculo("Caminhão", "Mercedes-Benz", "Actros", 2022, 2, 4)
caminhao_autoescola.observacao = "Caminhão para autoescola"
caminhao_autoescola.habilitacao_necessaria = habilitacao_C
caminhao_autoescola.tracao = "Automotor"
caminhao_autoescola.especie_veiculo = "Veículo de carga"
caminhao_autoescola.categoria_veiculo = "De aprendizagem"
print(caminhao_autoescola)

trator_pa = Veiculo("Trator Pá", "Caterpillar", "D6T", 2021, 1, 2)
trator_pa.observacao = "Veículo para obras"
trator_pa.habilitacao_necessaria = habilitacao_C
trator_pa.tracao = "Automotor"
trator_pa.especie_veiculo = "Veículo de tração"
trator_pa.categoria_veiculo = "Oficial"
print(trator_pa)

sedan = Veiculo("Corolla", "Toyota", "Corolla GLi 2.0", 2020, 5, 2)
sedan.observacao = "Excelente estado"
sedan.habilitacao_necessaria = habilitacao_B
sedan.tracao = "Automotor"
sedan.especie_veiculo = "Veículo de passageiro"
sedan.categoria_veiculo = "Particular"
print(sedan)

tesla = Veiculo("Model S", "Tesla", "Model S", 2022, 5, 2)
tesla.observacao = "Novo modelo"
tesla.habilitacao_necessaria = habilitacao_B
tesla.tracao = "Elétrico"
tesla.especie_veiculo = "Veículo de passageiro"
tesla.categoria_veiculo = "Oficial"
print(tesla)

bicicleta = Veiculo("Bicicleta", "Caloi", "XRT", 2021, 1, 2)
bicicleta.observacao = "Muita saúde"
bicicleta.tracao = "Propulsão humana"
bicicleta.especie_veiculo = "Veículo de passageiro"
bicicleta.categoria_veiculo = "De representação diplomática"
print(bicicleta)

carroca_cavalo = Veiculo("Carroça de Cavalo", "Madeira", "Carrox", 2019, 2, 2)
carroca_cavalo.observacao = "Rápido"
carroca_cavalo.habilitacao_necessaria = habilitacao_A
carroca_cavalo.tracao = "Tração animal"
carroca_cavalo.especie_veiculo = "Veículo de tração"
carroca_cavalo.categoria_veiculo = "Particular"
print(carroca_cavalo)

carreta = Veiculo("Carreta", "Randon", "Forte", 2018, 2, 4)
carreta.observacao = "Capacidade de carga 20 toneladas"
carreta.habilitacao_necessaria = habilitacao_C
carreta.tracao = "Reboque"
carreta.especie_veiculo = "Veículo de carga"
carreta.categoria_veiculo = "Oficial"
print(carreta)

carro_competicao = Veiculo("F1 Car", "Ferrari", "SF21", 2021, 1, 4)
carro_competicao.observacao = "Carro para competição"
carro_competicao.habilitacao_necessaria = habilitacao_B
carro_competicao.tracao = "Automotor"
carro_competicao.especie_veiculo = "Veículo de competição"
carro_competicao.categoria_veiculo = "Particular"
print(carro_competicao)

trator2 = Veiculo("Trator", "John Deere", "X350", 2020, 1, 2)
trator2.observacao = "Outro trator"
trator2.habilitacao_necessaria = habilitacao_C
trator2.tracao = "Automotor"
trator2.especie_veiculo = "Veículo especial"
trator2.categoria_veiculo = "Oficial"
print(trator2)

carro_colecao = Veiculo("Beetle", "Volkswagen", "1967", 1967, 4, 2)
carro_colecao.observacao = "Carro clássico para coleção"
carro_colecao.habilitacao_necessaria = habilitacao_B
carro_colecao.tracao = "Automotor"
carro_colecao.especie_veiculo = "Veículo de coleção"
carro_colecao.categoria_veiculo = "Particular"
print(carro_colecao)

carro_autoescola2 = Veiculo("Civic", "Honda", "2020", 2020, 5, 2)
carro_autoescola2.observacao = "Carro para carro autoescola"
carro_autoescola2.habilitacao_necessaria = habilitacao_B
carro_autoescola2.tracao = "Automotor"
carro_autoescola2.especie_veiculo = "Veículo de passageiro"
carro_autoescola2.categoria_veiculo = "De aprendizagem"
print(carro_autoescola2)

triciclo = Veiculo("Triciclo", "Generic", "Model T", 2020, 2, 2)
triciclo.tracao = "Propulsão humana"
triciclo.especie_veiculo = "Veículo misto"
triciclo.categoria_veiculo = "De representação diplomática"
print(triciclo)