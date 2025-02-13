import pandas as pd
import matplotlib.pyplot as plt

# ==============================================================
# GRÁFICO PIZZA
# ==============================================================

plt.title('Eleição 2024')

votos = (
    8567, 8128, 6912, 6409, 6371,
    6314, 6271, 6131, 5355, 5050,
    5003, 4982, 4782, 4641, 4577,
    4576, 4236, 4179, 4148, 4119,
    4063, 4030, 4022, 3859, 3768, 
    3636, 3244, 3167, 2426, 3922
)

candidatos = [
    'Marquinhos Trad', 'Rafael Tavares', 'Carlão Comunitário Mesmo','Silvio Pitu', 'Veterinário Francisco',
    'Fabio Rocha', 'Professor Riverton','Junior Coringa', 'Dr Victor Rocha', 'Professor Juari', 
    'Flavio Cabo Almi', 'Luiza Ribeiro', 'André Salineiro Agente Federal', 'Papy', 'Ana Portela',
    'Neto Santos','Maicon Nogueira', 'Delei Pinheiro', 'Wilson Lands', 'Herculano Borges',
    'Beto Avelar', 'Dr Jamal', 'Landmark', 'Clodoilson Pires', 'Jean Ferreira',
    'Dr Lívio', 'Ronilço Guerreiro', 'Leinha', 'Otávio Trad', 'Dr Sandro'
]

plt.pie(
    votos,
    labels=candidatos, 
    autopct='%.2f%%',
    shadow=True
)

plt.show()

# ==============================================================
# GRÁFICO BARRA
# ==============================================================

plt.title('Eleição 2024')

votos = (
    8567, 8128, 6912, 6409, 6371,
    6314, 6271, 6131, 5355, 5050,
    5003, 4982, 4782, 4641, 4577,
    4576, 4236, 4179, 4148, 4119,
    4063, 4030, 4022, 3859, 3768, 
    3636, 3244, 3167, 2426, 3922
)

candidatos = [
    'Marquinhos Trad', 'Rafael Tavares', 'Carlão Comunitário Mesmo','Silvio Pitu', 'Veterinário Francisco',
    'Fabio Rocha', 'Professor Riverton','Junior Coringa', 'Dr Victor Rocha', 'Professor Juari', 
    'Flavio Cabo Almi', 'Luiza Ribeiro', 'André Salineiro Agente Federal', 'Papy', 'Ana Portela',
    'Neto Santos','Maicon Nogueira', 'Delei Pinheiro', 'Wilson Lands', 'Herculano Borges',
    'Beto Avelar', 'Dr Jamal', 'Landmark', 'Clodoilson Pires', 'Jean Ferreira',
    'Dr Lívio', 'Ronilço Guerreiro', 'Leinha', 'Otávio Trad', 'Dr Sandro'
]

plt.bar(candidatos, votos)

plt.show()