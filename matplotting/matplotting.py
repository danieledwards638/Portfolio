import matplotlib.pyplot as plt
import numpy as np

x=np.array([87,86,47,73,65,100,83,100])
titles=np.array(['1','2','3','4','5','6','7','8'])


plt.pie(x,labels=titles)
plt.title("Units Average")
plt.legend()

plt.show()