N,L = map(int,input().split())
K=int(input())
A = list(map(int, input().split()))
left =0
right = L

mid = int((left+right)/2)

# midが最大値になるならTrueを返す
def check(mid):
    cut = 0
    count = 0
    
    for i in A:
        if(count==K):
            break
        
        if((i-cut)>=mid):
            cut = i
            count += 1
    
    if(L-cut>=mid and count==K):
        return True
    else:
        return False

while (right-left>1):
    if (check(mid)):
        left = mid
    else:
        right = mid
        
    mid = int((left+right)/2)
print(left)
        
    