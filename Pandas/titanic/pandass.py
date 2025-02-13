import pandas as pd

print (pd.__version__)

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# print(df.head()) #print o começo da lista - 5 primeiros
# print(df.tail()) #print o fim da lista - 5 ultimos
# print(df.info()) #descreve a tabela

df.set_index('PassengerId', inplace=True) #define uma nova índice(por padrao começa no 0)
# print(df.head(12))

# print(df.columns) #print colunas
# print(df.values) #print apenas os valores dos campos

# print(df.loc[1]) #retorna todas as informações da linha escolhida de acordo com o id
# print(df.loc[[1,2,3]]) #retorna todas as informações da linha escolhida de acordo com o id, para mais de uma linha usar lista[]

# print(df.loc[[1,2]], ['Name', 'Sex', 'Age']) #retorna todas as informações da linha escolhida de acordo com o id, para mais de uma linha usar lista[]

# print(df.loc[10:20]) #retorna as informações de um trecho a outro

# print(df.loc[10:30:2]) #retorna as informações de um trecho a outro pulando quantas linhas definir

# print(df.loc[1:10, ['Name', 'Sex', 'Age']])  #retorna todas as informações da linha escolhida de acordo com o id + as colunas escolhidas

# print(df.query('Age >20').head())

# print(df.query('Age > 20'))

print(df.query ('Age > 20 & Sex=="male"').head())

df.to_csv('dataset.csv', sep=';', index=False, encoding='utf-8-sig') #Salva o csv com as alterações feitas
#---- Nome do arq--Separador dos dados--Deixa definido a indice escolhida---linguagem do teclado

