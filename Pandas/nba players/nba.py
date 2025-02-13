import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("all_seasons.csv")

df1 = df.loc[0:11145, ["player_height"]]
df2 = df.loc[0:11145, ["player_weight"]]

plt.scatter(df1, df2)

plt.show()