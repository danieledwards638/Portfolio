import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("pokemon.csv")
#height_m
#speed
#weight_kg
#name

tallest = df.loc[df['height_m'].idxmax()].japanese_name
fastest = df.loc[df['speed'].idxmax()].japanese_name
heaviest = df.loc[df['weight_kg'].idxmax()].japanese_name

print(f'The tallest pokemon is {tallest}\nThe fastest pokemon is {fastest}\nThe heaviest pokemon is {heaviest}')

names=df['name']
heights=df['height_m']
speeds=df['speed']
weights=df['weight_kg']

plt.plot(heights)
plt.plot(speeds)
plt.plot(weights)
plt.legend(['Height','Speed','Weight'])
plt.title('Heights, Speeds and Weights of every pokemon on a graph')
plt.show()