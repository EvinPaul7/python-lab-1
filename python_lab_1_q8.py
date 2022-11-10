import random
a=int(input("Guess the number: "))
b=random.randint(1,9)
if a < b:
        print(str(a) + " is too low , The correct answer is", b)
elif a== b:
        print(b, " is correct")
else:
        print(str(a) + " is too high , The correct answer is", b)


