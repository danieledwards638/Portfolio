import pandas as pd
import random
df= pd.read_csv('assets/Task4a_data.csv')
index=random.randint(0,len(df)-1)
print((df.iloc[index])['Question'])
print('A. '+(df.iloc[index])['A'])
print('B. '+(df.iloc[index])['B'])
print('C. '+(df.iloc[index])['C'])
print('D. '+(df.iloc[index])['D'])
print('\n'+(df.iloc[index])['Answer'])