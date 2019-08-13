n=int(input("enter the number of elements of the list:"))
list1=[]
for i in range(n):
    ele=int(input("enter the elements:"))
    list1.append(ele)
    list2=[]
for num in list1 :
    if num%2==0 :
     list2.append(num)
for i in list2:
    print("even numbers of the list are:",i)
