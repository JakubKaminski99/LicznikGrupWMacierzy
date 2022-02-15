import random
print("Hello, let's play rock, paper, scissors ")

actions = ["Rock", "Paper", "Scissors"]
lose = False

while lose != True:
    bot = actions[random.randint(0,2)]
    print(bot)
    player = input("Rock, Paper, Scissors... ")
    if(player==bot):
        print("Draw")
    else:
        if(player=="Rock" and bot == "Scissors"):
            print("You win! ")
        elif(player=="Scissors" and bot == "Paper"):
            print("You win! ")
        elif(player=="Paper" and bot == "Rock"):
            print("You win! ")
        else:
            print("Bot win ")
            lose = True