a =input("Enter string : ") 

reverse ="" 

for x in a: 
   reverse=x + reverse  
print("Reverse of the string is : ", reverse)

if(reverse==a):
    print("The value", a, "is a palindrome")
else:
    print("The value", a, "is not a palindrome")
 
