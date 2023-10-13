'''def bs_floor(l,target):
    start=0
    end=len(l)-1
    floor=-1
    while(start<end):
        mid=((start+end)//2)
        if l[mid]==target:
            print(l[mid])
            break
        elif l[mid]<target:
            floor=l[mid]
            start=mid+1
        else:
            end=mid-1'''
def bs_floor(l,target,si,li,floor):
    if si<=li:
        mid=(si+li)//2
        if l[mid]==target:
            return l[mid]
        if l[mid]<target:
            floor=l[mid]
            return bs_floor(l,target,mid+1,li,floor)
        else:
            return bs_floor(l,target,si,mid-1,floor)
            li=mid-1
    return floor
    '''if si>li:
        return''' 
l=[2,6,8,9,10]
target=7
print(bs_floor(l,target,si,li,floor))
