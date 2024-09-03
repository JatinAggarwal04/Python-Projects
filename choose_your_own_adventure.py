name=input("Type your name: ")
print("Welcome", name, "to this adventure!")
answer=input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()
if answer=="left":
    answer=input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross ").lower()
    if answer=="swim":
        print("You swam across and were eaten by an alligator")
    elif answer=="walk":
        print("You walked around for many miles, ran out of water and lost the game")
    else:
        print("Not a valid option. You lose.")
elif answer=="right":
    answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)").lower()
    if answer=="back":
        print("You go back and lose.")
    elif answer=="cross":
        answer=input("You can cross the bridge and meet a stranger. DO you talk to the stranger(Y/N)").lower()
        if answer=="y":
            print("You talk to the stranger and they give you money.YOU WIN!!!!")
        elif answer=="n":
            print("You lose")
        else:
            print("Not a valid option. You lose")
else:
    print("Not a valide option. You lose")
print("Thank You for playing")