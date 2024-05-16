N,K = list(map(int, input().split()))
A = list(map(int, input().split()))

startCount =0
emptyCount = K

for i in A:
    if emptyCount >= i:
        emptyCount -= i
    else:
        startCount += 1
        emptyCount = K
        emptyCount -= i

if emptyCount != K:
    startCount += 1
    
print(startCount)