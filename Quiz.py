print("Welcome to the quiz")
question=""
answer=""

def question(question, answer, points):
    response = input(question)
    if(response.lower() == answer):
        print("Correct!")
        points += 1
        print(points)
    else:
        print("Nope")
    return points

game=input("Wanna play again? Yes/No ")
while(game.lower()=="yes"):
    points = 0
    points=question("How are you? ", "fine", points)
    points=question("Ok? ", "no", points)
    points=question("Yes? ", "yes", points)
    print(f"Your score is  {points}, nice")
    game=input("Wanna play again? Yes/No ")
