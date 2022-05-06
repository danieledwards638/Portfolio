import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("scottish_hills.csv")
x=df.Height
y=df.Latitude
plt.scatter(x,y)
plt.show()