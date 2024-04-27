import random

#randNum = random.randint(1,5)

target = random.randint(1,100)
while True:
    userChoice = int(input("Guess the target or Quit(Q): "))
    if(userChoice == "Q" or userChoice == "q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success: Correct Guess!..")
        break
    elif(userChoice < target):
        print("your number was too samll. Take a bigger guess....")
    else:
        print("your number was too large. Take a smaller guess....")    


print("-----Game Over-----")    