import pandas as pd
import matplotlib.pyplot as plt

# ==============================================================
# GRÁFICO PIZZA
# ==============================================================

plt.title('Eleição 2024 - Prefeito Corumbá', fontsize=14)

votos = (
   28394, 10659, 5944, 5043
)

candidatos = [
    'Dr. Gabriel', 'Luiz Antonio Pardal',
    'André Campos', 'Delcídio Amaral'
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

plt.title('Eleição 2024 - Prefeito Corumbá', fontsize=14)

votos = (
   28394, 10659, 5944, 5043
)

candidatos = [
    'Dr. Gabriel', 'Luiz Antonio Pardal',
    'André Campos', 'Delcídio Amaral'
]

plt.bar(candidatos, votos)

plt.show()