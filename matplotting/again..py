import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open('bldprs.csv', 'r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
    plt.scatter(x,y,color='g',marker='o',label="Blood Pressure")
    plt.xticks(rotation=25)
    plt.xlabel('Names')
    plt.ylabel('Values')
    plt.title('Patients Blood Pressure', fontsize=20)
    plt.grid()
    plt.legend()
    plt.show()