import random 
import string

def generate_password(min_length, numbers=False, special_characters=False):
   letters=string.ascii_letters
   digits=string.digits  
   special=string.punctuation

   characters=letters
   if numbers:
      characters+=digits
   if special_characters:
      characters+=special   
      
   password=""
   
   while min_length< or min_length>50:
        if min_length==max(min_length, 50):
           min_length=int(input())
           print("Enter min_length of the password: ")
           return generate_password(min_length, numbers, special_characters)
        elif characters==numbers:
              print("Include numbers? (y/n): ")
              include_numbers=int(input())
              if include_numbers==1:
                 characters+=digits
        elif characters==special:
              print("Include special characters? (y/n): ")
              include_special=int(input())
              if include_special==1:
                 characters+=special
        else:
            break
        for i in range(min_length):
            password+=random.choice(characters)
        return password
password=generate_password(8)
print("Generated password: ",password)