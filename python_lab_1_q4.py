

num = int(input("Enter a number to find all it's divisible: "))

answer = []

for x in range(2,num):
    if num % x == 0:
        answer.append(x)
print(answer)