#Agressive cows
def isvalid(k,stalls,mid):
    prevcow=stalls[0]
    count=1
    for i in stalls:
        if (i-prevcow)>=mid:
            count+=1
            prevcow=i
    return True if k==count else False
def solve(n,k,stalls):
    stalls.sort()
    si=stalls[0]
    li=stalls[-1]
    res=0
    while si<=li:
        mid=(si+li)//2
        if isvalid(k,stalls,mid):
            res=mid
            si=mid+1
        else:
            li=mid-1
n=5
k=3
stalls
