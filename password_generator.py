import random
import string

length=int(input("enter the length of password: "))

characters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation

combine=characters+numbers+symbols

temp=random.sample(combine,length)

password="".join(temp)

print("password: ",password)
