import pandas as pd
import matplotlib.pyplot as plt


# ==============================================================
# GRÁFICO PIZZA
# ==============================================================

plt.title('Eleição 2024 - Prefeitura Dourados', fontsize=14)

votos = (
    60418, 34027, 17845, 5476, 2455, 377, 117
)

candidatos = [
    'Marçal Filho', 'Alan Guedes', 'Tiago Botelho', 'Bela Barros',
    'Racib Harb', 'Beto Teles','Valderi Garcia'
]

plt.pie(
    votos,
    labels=candidatos,
    autopct='%.2f%%',
    shadow=True, 
    textprops={'fontsize': 8}
)

plt.show()

# ==============================================================
# GRÁFICO BARRA
# ==============================================================

plt.title('Eleição 2024 - Prefeitura Dourados', fontsize=14)

votos = (
    60418, 34027, 17845, 5476, 2455, 377, 117
)

candidatos = [
    'Marçal Filho', 'Alan Guedes', 'Tiago Botelho', 'Bela Barros',
    'Racib Harb', 'Beto Teles','Valderi Garcia'
]

plt.bar(candidatos, votos)

plt.show()