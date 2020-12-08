def main():
    a=[[1,2,3],[6,7,8],[4,5,9]]
    m=3
    suum=0
    for i in range(0,m):
        suum=suum+a[i][m-i-1]
    sr=suum/m
    print(sr)
main()
