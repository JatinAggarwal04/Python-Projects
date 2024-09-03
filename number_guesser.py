import random
top_of_range=input("Type a number for range of random number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please type a number larger than 0 nect time.")
else:
    print('Please type a number next time !')
    quit()
random_number=random.randint(0,top_of_range)
count=0
while True:
    count+=1
    guess=input("Guess the random number: ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print('Please type a number next time.')
        continue
    if guess == random_number:
        print("Congratulations you have successfully guessed the number in", count, "guesses")
        break
    elif guess>random_number:
        print("You were above the number !!!")
    else:
        print("You were below the number")

