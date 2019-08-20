def search(lis,a):
    if a in lis:
        return True
    else:
        return False
lis=[]
while True:
    a=int(input("enter the elements:"))
    if a!=-1:
        lis.append(a)
    else:
        break
b=int(input("enter the number to be searched:"))
print(search(lis,b))
    
