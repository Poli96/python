a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=int(input("Введите третье число: "))
k=0
def main(a,b,c,k):
    if a>0:
       k+=1
    if b>0:
       k+=1
    if c>0:
       k+=1
    print(k)
main(a,b,c,k)
