# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def isPrime(n):
     if n<1 or n>2*(10**9): 
         return 0 
     if n == 1:
          return 0 
     if n == 2:
              return 1 
     for i in range(2,n): 
         if n%i == 0: 
             return 0 
     return 1
def isPrime2(n):
     if n<1 or n>2*(10**9):
          return 0
     if n == 1:
         return 0
     if n%2 == 0:
         return n==2 
     if n%3 == 0:
         return n==3
     if n%5 == 0:
         return n==5 
     for i in range(7,int(math.sqrt(n))+1):
         if n%i == 0:
             return 0
     return 1 
     T = input().strip()
     if int(T)<1 or int(T)>30:
         print("T<1 or T>30") 
     else:
         for i in range(int(T)): 
             n = input().strip() 
             flag = isPrime2(int(n))
             if flag:
                 print("Prime") 
             else:
                 print("Not prime")



