import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.set_index('PassengerId', inplace=True)

criancas = df.query('Age < 10 and Survived == 1')
criancas.to_csv('CriançasSobreviventes.csv', sep=';', index=False, encoding='utf-8-sig')

mulheres = df.query('Sex == "female" and Survived == 1')
mulheres.to_csv('MulheresSobreviventes.csv', sep=';', index=False, encoding='utf-8-sig')

homens = df.query('Sex == "male" and Survived == 1')
homens.to_csv('HomensSobreviventes.csv', sep=';', index=False, encoding='utf-8-sig')

idosos = df.query('Sex == "male" and Age > 50 and Survived == 1')
idosos.to_csv('IdososSobreviventes.csv', sep=';', index=False, encoding='utf-8-sig')

criancas2 = df.query('Age < 12 and Sex == "female" and Survived == 1')
criancas2.to_csv('CriançasSobreviventes2.csv', sep=';', index=False, encoding='utf-8-sig')
