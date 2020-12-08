def revers(Ks):
    return Ks[::-1]

def IsPalindrom(k):
    Ks=str(k)
    if (Ks==revers(Ks)):
        return True
    else:
        return False
R=0
n=int(input("Введите количество чисел n="))
for i in range(0,n):
    k=int(input("Введите число К="))
    if IsPalindrom(k)==True:
        R+=1
print("Количество палиндромов=",R)
