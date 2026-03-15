import random
import string

length=int(input("Enter the length of the password: " ))

print('''Enter the choice for the password: 1. letters /n 2. Digits /n 3. special characters /n 4. Exit''')

characters=""
while True:
    choice=int(input("Pick a number: "))
    if(choice==1):
        characters+=string.ascii_letters
    elif(choice==2):
        characters+=string.digits
    elif(choice==3):
        characters+=string.punctuation
    elif choice==4:
        break
    else:
        print("Please enter a valid choice")
password=[]
for i in range(length):
    randomchar=random.choice(characters)
    password.append(randomchar)
print("Generated password: "+"".join(password))
    
    