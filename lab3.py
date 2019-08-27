import random
import string
chars=string.printable
n=int(input("enter the length of the password"))
for i in range(n):
    a=str("".join(random.sample(chars,n)))
print(a)
