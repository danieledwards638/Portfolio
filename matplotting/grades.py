import matplotlib.pyplot as plt
import csv
Subjects = []
Scores=[]

with open('grades.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
        Subjects.append(row[0])
        Scores.append(int(row[1]))
    plt.pie(Scores,labels=Subjects,autopct = '%2f%%')
    plt.title('Student Grades',fontsize = 20)
    plt.show()