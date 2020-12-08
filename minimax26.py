def main():
    arr=[4,8,4,6,8,5,3,1,7,9]
    k=[]
    maxx=0
    for i in arr:
        if (i%2==0):
            maxx+=1
        else:
            k.append(maxx)
    print(max(k))
main()
