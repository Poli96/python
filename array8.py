n=int(input("Введите количество чисел: "))
k=0
a=[]
print("Введите", n,"элеметов: ")
for i in range(0,n):
    x=int(input())
    if (x%2!=0):
        k+=1
        a.append(x)
print("Нечётные числа: ")
for i in range(0,k):
    print(a[i])
print("количество нечётный чисел=",k)
