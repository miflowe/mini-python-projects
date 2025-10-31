import random

print("===================\nRock Paper Scissors\n===================\n1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖")
# Rock=1     Paper=2     Scissors=3      Lizard=4     Spock=5
# 1>3        2>1           3>2            4>5          5>3
# 1>4        2>5           3>4            4>2          5>1

rock = "✊"
paper = "✋"
scissors = "✌️"
lizard = "🦎"
spock = "🖖"

player = int(input("Pick a number: "))
computer = random.randint(1, 5)
if computer == 1:
    computer = rock
elif computer == 2:
    computer = paper
elif computer == 3:
    computer = scissors
elif computer == 4:
    computer = lizard
elif computer == 5:
    computer = spock

if player == 1:
    print(f"You chose: {rock}")
    print(f"CPU chose: {computer}")
    if computer == scissors or computer == lizard:
        print("You won!")
    elif computer == player:
        print("You tied!")
    else:
        print("You lost!")

elif player == 2:
    print(f"You chose: {paper}")
    print(f"CPU chose: {computer}")
    if computer == rock or computer == spock:
        print("You won!")
    elif computer == player:
        print("You tied!")
    else:
        print("You lost!")

elif player == 3:
    print(f"You chose: {scissors}")
    print(f"CPU chose: {computer}")
    if computer == paper or computer == lizard:
        print("You won!")
    elif computer == player:
        print("You tied!")
    else:
        print("You lost!")

elif player == 4:
    print(f"You chose: {lizard}")
    print(f"CPU chose: {computer}")
    if computer == paper or computer == spock:
        print("You won!")
    elif computer == player:
        print("You tied!")
    else:
        print("You lost!")

elif player == 5:
    print(f"You chose: {spock}")
    print(f"CPU chose: {computer}")
    if computer == rock or computer == scissors:
        print("You won!")
    elif computer == player:
        print("You tied!")
    else:
        print("You lost!")

else:
    "You entered an invalid number. Ending run."
