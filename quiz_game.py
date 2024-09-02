print("Welcome to my computer quiz!")

playing=input("Do you want to play?(Y/N) ").upper()
if playing !="Y":
    quit()

print("OK! Let's Play")
points=0
answer=input("What does CPU stand for? ")

if answer.lower()=="central processing unit":
    print("Correct!")
    points+=1
else:
    print("InCorrect!")

answer=input("Which is the latest iPhone? ")

if answer.lower()=="iphone 15":
    print("Correct!")
    points+=1
else:
    print("InCorrect!")

answer=input("What does RAM stand for?")

if answer.lower()=="Random Access Memory":
    print("Correct!")
    points+=1
else:
    print("Incorrect!")
print("You have scored "+str(points)+" points")