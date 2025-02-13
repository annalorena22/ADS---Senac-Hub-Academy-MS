import pandas as pd
import matplotlib.pyplot as plt

# ==============================================================
# GRÁFICO PIZZA
# ==============================================================

plt.title('Eleição 2024 - Prefeitura Campo Grande', fontsize=14)

votos = (
    140913, 131525, 115516, 41966, 10885, 3108, 1067
)

candidatos = [
    'Adriane Lopes', 'Rose Modesto', 'Beto Pereira','Camila Jara',
    'Beto Figueiró', 'Luso de Queiroz','Ubirajara Martins'
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

plt.title('Eleição 2024 - Prefeitura Campo Grande', fontsize=14)


votos = (
    140913, 131525, 115516, 41966, 10885, 3108, 1067
)

candidatos = [
    'Adriane Lopes', 'Rose Modesto', 'Beto Pereira','Camila Jara',
    'Beto Figueiró', 'Luso de Queiroz','Ubirajara Martins'
]

plt.bar(candidatos, votos)
plt.show()