s=0
while True:
    a=int(input())
    if ((a>0) and (a%2==0)):
        s+=a
    if (a==0):
        break
print(s)
