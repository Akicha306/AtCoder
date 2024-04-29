N, K = map(int, input().split())
A = list(map(int, input().split()))

sum = K*(K+1)//2

appearList = []

def existList(n):
    for i in appearList:
        if(i == n):
            return True
    return False

for i in A:
    if(i>K):
        continue
    
    
print(sum)    
