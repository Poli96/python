def main():
    n=10
    maxx=0
    nomer=0
    b=int(input("Введите число В(0<В<C): "))
    c=int(input("Введите число C(0<В<C): "))
    print("Введите", n,"элементов:")
    for i in range(1,n+1):
        x=int(input())
        if ((x>b) and (x<c)):
            if ((nomer==0) or (maxx<x)):
                maxx=x
                nomer=i
    if (nomer>0):
        print("Максимальный элемент между", b,"и", c,": ", maxx,".","Его номер: ", nomer)
    else:
        print(0, 0)
main()
