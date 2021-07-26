import random
number=random.randint(1,20)
chance=0

while (chance<5):
    guess = int(input("guess the no: "))
    if (guess<number):
        print("guess is bit low")
    elif(number<guess):
        print("guess is to high")
    elif(number==guess):
        print("tusi git gaya ho")