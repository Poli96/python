x=int(input(""))
s=x
n=int(input(""))
if x!=0:
    a=x
    for i in range(2,n+1):
        a=-a*x
        s=s+a/i
print(s)
