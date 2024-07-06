N,wMax = list(map(int, input().split()))

A = []
W = []
for _ in range(N):
    a,w = list(map(int, input().split()))
    A.append(a)
    W.append(w)
    
dp = [[0 for _ in range(wMax+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,wMax+1):
        if W[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i-1]] + A[i-1])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[-1][-1])