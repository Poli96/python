B=float(input())
print("B= ",B)
N=int(input())
print("N= ",N)
for i in range(1,N+1):
    print(i,end="; ")
flag = True
for i in range(1,N+1):
    print(i,end="; ")
    if ((i<=B) and (B<i+1)):
        print("B:",B,end="; ")
        flag=False
