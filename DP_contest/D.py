
W = int(input())
N, K = [int(a) for a in input().split()]

A = []
B = []
for _ in range(N):
    a, b = [int(a) for a in input().split()]
    A.append(a)
    B.append(b)

dynamicList = [[0 for _ in range(W+1)] for _ in range(N+1)]
countList = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, W+1):
        if A[i-1] <= j and countList[i-1][j-A[i-1]]+1 <= K:
            dynamicList[i][j] = max(
                dynamicList[i-1][j-A[i-1]]+B[i-1], dynamicList[i-1][j])
            countList[i][j] = countList[i-1][j-A[i-1]]+1
        else:
            if(countList[i-1][j-A[i-1]]+1 > K) and (dynamicList[i][j-1] > dynamicList[i-1][j]):
            
                    dynamicList[i][j] = dynamicList[i][j-1]
                    countList[i][j] = countList[i][j-1]
            else:
                dynamicList[i][j] = dynamicList[i-1][j]
                countList[i][j] = countList[i-1][j]

print(dynamicList[N][W])
