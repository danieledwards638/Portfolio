import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("weather.csv")
convert_date=df['Date']

legends=['Manchester','Orlando','Dallas','Los Angeles','Houston']

tempman=df['Man']
temporl=df['Orl']
tempdal=df['Dal']
templa=df['LA']
temphous=df['Hous']

plt.plot_date(convert_date,tempman,linestyle='solid',color='c',marker='.')
plt.plot(temporl,marker='.')
plt.plot(tempdal,marker='.')
plt.plot(templa,marker='.')
plt.plot(temphous,marker='.')
plt.xticks(rotation=25)
plt.legend(legends)
plt.plot()
plt.title('Weather for 5 cities in the world')
plt.show()