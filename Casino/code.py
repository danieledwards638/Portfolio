import random
import colorama
from colorama import Fore


def play(Mone):
    colorama.init()  
    tokens=Mone
    symbols = ["@", "#", "$"]


    global highest_score
    highest_score = [100]
    print("Welcome to Kris's slot machine")
    while tokens > 0:
        print("You have",tokens,"tokens.")
        try:
            bet = int(input("Bet Amount: "))
        except:
            print("Please enter a valid Bet.")
            continue
        if bet > tokens:
            print("You cannot bet that much.")
        else:
            tokens = tokens - bet
        s_one = random.choice(symbols)
        s_two = random.choice(symbols)
        s_three = random.choice(symbols)
        print()
        print("-------------")
        print("|", random.choice(symbols), "|", random.choice(symbols), "|", random.choice(symbols), "|")
        print(Fore.YELLOW + "-------------")
        print("|", s_one, "|", s_two, "|", s_three, "|")
        print("-------------")
        print(Fore.WHITE + "|", random.choice(symbols), "|", random.choice(symbols), "|", random.choice(symbols), "|")
        print("-------------")
        if s_one == s_two and s_two == s_three:
            win = bet * 5
            tokens = tokens + win
            print("You Have Won",win,"Good Job.")
            highest_score.append(tokens)
        else:
            print("You have lost")
    print("You are out of tokens")
    high_score = max(highest_score)
    while True:
        save = input("Would you like to save your score to a leaderboard?(Y/N)").lower()
        if save == "y":
            name = input("What is your name?")
            file = open("LeaderBoard.txt", "a")
            file.write("\n""Name = "+ name + "\n" + "Highest Tokens = "+ str(high_score))
            file.close
            break
        elif save == "n":
            print("Thank you for playing")
            break
        else:
            print("Invalid input, try again")
        continue
    return tokens


