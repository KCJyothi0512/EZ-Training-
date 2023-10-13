W=int(input())
wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
perkg=[]
'''for i in range(len(wt)):
    perkg.append(pr[i]/wt[i])'''
l=list(zip(wt,pr,perkg))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
maxpr=0
for weight,profit in l:
    if weight<=W:
        maxpr+=profit
        W-=weight
    else:
        maxpr+=W*(profit/weight)
        break
print(maxpr)
