#print 1 to n using recursion
n=int(input())
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)
fun(n)
