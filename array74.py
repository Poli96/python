def main():
    a=[1,2,3,4,5,9,2,5,8,6]
    n=10
    miin=100000000
    maax=0
    simvmin=0
    simvmax=0
    for i in range(0,n):
        if (miin==0) or (miin>a[i]):
            miin=a[i]
            simvmin=i
        if (maax==0) or (maax<a[i]):
            maax=a[i]
            simvmax=i
    for i in range(simvmin+1,simvmax):
        a[i]=0
    for i in range(0,n):
        print(a[i])
main()
