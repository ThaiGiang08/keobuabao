from random import randint

print("Nhap Dam, La, Keo:")
player = input()
computer = randint (0,2)

           
if computer == 0:
    computer = "Bua"
if computer == 1:
    computer = "Bao"
if computer == 2:
    computer = "Keo"

print("___")
print("You choose: " + player)
print("Computer chooses: " + computer)
print("___")

if player == computer:
    print("Draw")
else:
    if computer == "Bua":
            print("Lose")
        else:
            print ("Win")

    elif player "Bua":
        if computer == "Keo"
            print("Win")
        else:
            print ("Lose")

    elif player "Bao":
        if computer == "Keo"
            print("Lose")
        else:
            print("Win")

    else:
        print("Nhap sai!")
