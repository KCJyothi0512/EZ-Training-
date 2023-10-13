def toh(n,src,aux,dest):
    if n>0:
        toh(n-1,src,dest,aux)
        print(src,dest)
        toh(n-1,aux,src,dest)
n=int(input())
toh(n,'A','B','C')
