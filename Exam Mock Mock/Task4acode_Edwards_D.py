import pandas as pd
import json
import random
import getpass
import datetime
import time

user = []



def play():
    total=0
    name=input("Enter your name.\n")
    date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n==========START QUIZ==========")
    score = 0
    df=pd.read_csv('assets/Task4a_data.csv')
    for i in range(10):
        no_of_questions = len(df)
        check = random.randint(0, no_of_questions - 1)
        print((df.iloc[check])['Question'])
        print('A. '+(df.iloc[check])['A'])
        print('B. '+(df.iloc[check])['B'])
        print('C. '+(df.iloc[check])['C'])
        print('D. '+(df.iloc[check])['D'])
        answer = input("\nEnter your answer: ")
        if answer.upper()==df.iloc[check]['Answer']:
            print("\nYou are correct.")
            score += int((df.iloc[check])['Mark'])
            total += int((df.iloc[check])['Mark'])
        else:
            print("\nYou are incorrect.")
            total += int((df.iloc[check])['Mark'])
    percentage = int(score/total*100)
    
    print(f'\nTOTAL SCORE: {score}')
    logs=pd.read_csv('assets/logs.csv')
    updaterow={'Date':date,'Name':name,'Score':(str(score)+"/"+str(total)),'Percentage':f"{percentage}%"}
    logs=logs.append(updaterow, ignore_index=True)
    logs.to_csv('assets/logs.csv',index=False)
    



def quizQuestions():
    if len(user) == 0:
        print("Only an admin can add questions, please login to verify.")
    elif len(user) == 2:
        if user[1] == "ADMIN":
            df=pd.read_csv('assets/Task4a_data.csv',index_col='Index')
            print('\n==========ADD QUESTIONS==========\n')
            unit=input("Enter the Unit Number\n")
            ques = input("Enter the question that you want to add:\n")
            print("Enter the 4 options with character initials (A, B, C, D)")
            a=input()
            b=input()
            c=input()
            d=input()
            ans=input("What is the correct answer (A, B, C, D\n")
            marks=input("Input the amount of marks the question will award\n")
            newrow = {'Unit': unit,'Question': ques, 'A': a, 'B': b, 'C': c, 'D': d,'Answer': ans,'Mark':marks}
            df = df.append(newrow, ignore_index=True)
            df.to_csv('assets/Task4a_data.csv', index=False)
            print("Successfully added question\n")
        else:
            print("You don't have access to adding questions. Only admins are allowed to add questions.\n")


def addAccount():
    print("\n==========CREATE ACCOUNT==========")
    username = input("Enter your USERNAME: ")
    password = getpass.getpass(prompt='Enter your PASSWORD: ')
    with open('assets/user_accounts.json', 'r+') as user_accounts:
        users = json.load(user_accounts)
        if username in users.keys():
            print("An account of this Username already exists.\nPlease enter the login panel.")
        else:
            users[username] = [password, "PLAYER"]
            user_accounts.seek(0)
            json.dump(users, user_accounts)
            user_accounts.truncate()
            print("Account created successfully!")


def loginAccount():
    print('\n==========LOGIN PANEL==========')
    username = input("USERNAME: ")
    password = getpass.getpass(prompt='PASSWORD: ')
    with open('assets/user_accounts.json', 'r') as user_accounts:
        users = json.load(user_accounts)
    if username not in users.keys():
        print("An account of that name doesn't exist.\nPlease create an account first.")
    elif username in users.keys():
        if users[username][0] != password:
            print("Your password is incorrect.\nPlease enter the correct password and try again.")
        elif users[username][0] == password:
            print("You have successfully logged in.\n")
            user.append(username)
            user.append(users[username][1])


def logout():
    global user
    if len(user) == 0:
        print("You are already logged out.")
    else:
        user = []
        print("You have been logged out successfully.")


def rules():
    print('''\n==========HOW TO PLAY==========
1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.
	''')


def about():
    print('''\n==========ABOUT US==========
This project has been created by ACC Ltd.''')

def stats():
    logs=pd.read_csv('assets/logs.csv')
    print(logs)

def average():
    num=0
    name=input("Enter the name of the student you would like to average.\n")
    logs=pd.read_csv('assets/logs.csv')
    averages=dict(logs[logs['Name']==name]['Percentage'])
    averagekeys=list(averages.keys())
    for i in range(len(averages)):
        num+=int((averages[averagekeys[i]])[:2])
    print(f'{name}s average percentage is '+str(int(num/len(averages)))+'%')


if __name__ == "__main__":
    choice = 1
    while choice != 7:
        print('\n=========ACC: QUIZ MASTER==========')
        print('-----------------------------------------')
        print('1. PLAY QUIZ')
        print('2. ADD QUIZ QUESTIONS')
        print('3. CREATE AN ACCOUNT')
        print('4. LOGIN')
        print('5. LOGOUT')
        print('6. HOW TO PLAY')
        print('7. EXIT')
        print('8. ABOUT US')
        print('9. LEARNER STATS')
        print('10. AVERAGE USER')
        choice = int(input('ENTER YOUR CHOICE: '))
        if choice == 1:
            play()
        elif choice == 2:
            quizQuestions()
        elif choice == 3:
            addAccount()
        elif choice == 4:
            loginAccount()
        elif choice == 5:
            logout()
        elif choice == 6:
            rules()
        elif choice == 7:
            break
        elif choice == 8:
            about()
        elif choice == 9:
            stats()
        elif choice == 10:
            average()
        else:
            print('WRONG INPUT. ENTER THE CHOICE AGAIN')
        time.sleep(2)
