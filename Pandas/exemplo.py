# import pandas as pd
# import matplotlib.pyplot as plt

# #primeiro o eixo x, depois o eixo y (sempre)
# a = (1,2,3,4,5)
# b = (1,2,3,4,5)

# plt.xlabel(u'Alguns números x') #define um nome para o eixo x
# plt.ylabel(u'Alguns números y') #define um nome para o eixo y

# plt.title('Meu Gráfico') #Define um nome para o gráfico

# # plt.plot(a,b) #Traça uma linha que une os dois valores
# # plt.plot(a,b,'r--o') #Definindo cor e tipo da linha (ver tabela de comando de cores e de linha)

# plt.axis((0,6,0,20))

# # plt.scatter(a,b) #Mostra o gráfico sem linha

# # plt.bar(a,b) #Mostra o gráfico em barras

# # plt.hist(a,b)

# a = (10,20,30)
# explode=(0.1, 0, 0)
# labels = ["HB20", "Gol", "Fusca"]
# plt.pie(a, explode=explode, labels=labels, autopct='%.2f%%', shadow=True)
# plt.grid(True)
# plt.show() #Mostra o gráfico (tipo)

import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame de exemplo
data = {
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Criando subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # 1 linha, 2 colunas

# Gráfico de barras
df.plot(kind='bar', x='Categoria', y='Valores', ax=axs[0], color='skyblue')
axs[0].set_title('Gráfico de Barras')
axs[0].set_ylabel('Valores')

# Gráfico de pizza
axs[1].pie(df['Valores'], labels=df['Categoria'], autopct='%1.1f%%', startangle=90)
axs[1].set_title('Gráfico de Pizza')

# Ajustando layout
plt.tight_layout()
plt.show()
