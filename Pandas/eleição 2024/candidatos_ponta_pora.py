
import pandas as pd
import matplotlib.pyplot as plt

# ==============================================================
# GRÁFICO PIZZA
# ==============================================================

plt.title('Eleição 2024 - Prefeito Ponta Porã', fontsize=14)

votos = (
   26473, 15195, 8168, 1314
)

candidatos = [
    'Eduardo Campos', 'Pompilio Júnior',
    'Carlos Bernardo', 'Álvaro Soares'
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

plt.title('Eleição 2024 - Prefeito Ponta Porã', fontsize=14)

votos = (
   26473, 15195, 8168, 1314
)

candidatos = [
    'Eduardo Campos', 'Pompilio Júnior',
    'Carlos Bernardo', 'Álvaro Soares'
]

plt.bar(candidatos, votos)

plt.show()