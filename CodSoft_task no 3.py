import string
import random

l = int(input("Enter the length of the password: "))

print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

c = ""

while (True):
    choice = int(input("Enter choice from above (enter a number): "))
    if (choice == 1):
        c += string.ascii_letters
    elif (choice == 2):
        c += string.digits
    elif (choice == 3):
        c += string.punctuation
    elif (choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(l):
    char = random.choice(c)
    password.append(char)

def printpwd(password):
    print("The random password is :")
    x=len(password)
    for i in range(x):
        print(password[i], end="")

printpwd(password)