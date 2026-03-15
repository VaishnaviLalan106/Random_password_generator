import random 
import string

if __name__=="__main__":
   s1=string.ascii_letters
   #print(s1)
   s2=string.digits
   #print(s2)
   s3=string.punctuation
   #print(s3)
   length=int(input("Enter the length of the password: " )) #Handle Gibberish input
   s=[]
   s.extend(list(s1))
   s.extend(list(s2))
   s.extend(list(s3))
   #print(s)
   random.shuffle(s)
   #print(s)
   print("Your password is:")
   print("".join(random.sample(s,length)))
   #print("".join(s[0:length]))