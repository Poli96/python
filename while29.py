import math
e=int(input())
a1=1
a2=2
k=3
while abs(a2-a1)>=e:
    k+=1
    c=a2
    a2=(a1+2*a2)/3
    a1=c
print("",k)
print("",a1," ", a2)
