n=int(input("enter a number: "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if n==sum:
    print("YES IT IS ARMSTRONG NO")
else:
    print("NO IT IS NOT ARMSTRONG NO")
