tokens = 100
name = input("What is your name?")
file = open("LeaderBoard.txt", "a")
file.write("\n" "Name = "+ name + "\n" + "Final Tokens = "+ str(tokens))
file.close