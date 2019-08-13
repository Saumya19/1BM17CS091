def fun_fibo(n):
   if n <= 1:
       return n
   else:
       return(fun_fibo(n-1) + fun_fibo(n-2))
nt=int(input("enter the value of n"))
if nt<= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nt):
       print(fun_fibo(i))
