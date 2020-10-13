n=int(input())
r=0
l=1
for i in range (1,n+1):
    for j in range (1,n-i+1):
        l=l*j
        r=r+l
print(r+n)
