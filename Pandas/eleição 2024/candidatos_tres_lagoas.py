import pandas as pd
import matplotlib.pyplot as plt

# ==============================================================
# GRÁFICO PIZZA
# ==============================================================

plt.title('Eleição 2024 - Prefeito Três Lagoas', fontsize=14)

votos = (
    38076, 16027, 1392
)

candidatos = [
    'Dr Cassiano Maia', 'Dr Ruy Costa', 'Professor Vitor'
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
# ==============================================================plt.title('Eleição 2024 - Prefeito Três Lagoas', fontsize=14)

votos = (
    38076, 16027, 1392
)

candidatos = [
    'Dr Cassiano Maia', 'Dr Ruy Costa', 'Professor Vitor'
]

plt.bar(candidatos, votos)

plt.show()
