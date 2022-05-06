import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df=pd.read_csv("scottish_hills.csv")

x=df.Height
y=df.Latitude
stats=linregress(x,y)
m=stats.slope
b=stats.intercept

plt.scatter(x,y)
plt.plot(x,m*x+b,color="red")
plt.show()