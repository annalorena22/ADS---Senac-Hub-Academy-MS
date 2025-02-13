import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("user_behavior_dataset.csv")

#==================================================
#           Uso de SmartPhone por Idade           #
#==================================================

age = df.loc[0:, "Age"]
user = df.loc[0:, "User ID"]


plt.title("Uso de SmartPhone por Idade")
plt.ylabel("Quantidade de Usuários",  fontsize=11)
plt.xlabel("Idade",  fontsize=12)

plt.bar(age, user)


plt.show()

#==================================================
#           Uso de SmartPhone por Gênero         #
#==================================================

gender = df.loc[0:, "Gender"]
user = df.loc[0:, "User ID"]

plt.title("Uso de SmartPhone por Gênero")
plt.ylabel("Quantidade de Usuários",  fontsize=11)
plt.xlabel("Gênero",  fontsize=12)

plt.bar(gender,user)


plt.show()

#========================================================
#  Número de Apps Instalado por Modelo de SmarthPhone   #  
#========================================================

device = df.loc[0:, "Device Model"]
apps = df.loc[0:, "Number of Apps Installed"]

plt.title("Número de Apps Instalado por Modelo de SmarthPhone")
plt.ylabel("Número de Apps Instalados",  fontsize=11)
plt.xlabel("Modelo de Smarthphone",  fontsize=12)

plt.bar(device,apps)


plt.show()

#==================================================
#  Consumo de Bateria por Modelo de SmarthPhone   #
#==================================================

device = df.loc[0:, "Device Model"]
battery = df.loc[0:, "Battery Drain"]

plt.title("Consumo de Bateria por Modelo de SmarthPhone")
plt.ylabel("Consumo de Bateria (mAh/Dia)",  fontsize=11)
plt.xlabel("Modelo de Smarthphone",  fontsize=12)

plt.bar(device, battery)

plt.show()

#==================================================
#  Modelos de SmarthPhone Encontrados na Pesquisa #
#==================================================

modelos = df.loc[0:]

soma_de_modelos= {}

for i in modelos.get('Device Model'):
    if i in soma_de_modelos:
        soma_de_modelos[i] +=1
    else:
        soma_de_modelos[i] = 1

quantidade_modelos = []
modelos = []

for nome, valor in soma_de_modelos.items():
    quantidade_modelos.append(valor)
    modelos.append(nome)

plt.title("Modelos de SmarthPhone Encontrados na Pesquisa")

plt.pie(
    quantidade_modelos,
    labels=modelos,
    autopct='%.2f%%',
    shadow=True, 
    textprops={'fontsize': 8}
)

plt.show()