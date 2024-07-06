N,M = list(map(int, input().split()))
A = []

dp = [0 for _ in range(N+1)]    
dp[0] = 1

for _ in range(M):
    dp[int(input())] = -1
    
for i in range(1,len(dp)):
    dp_1,dp_2 = 0,0
    
    if dp[i] == -1:
        continue
    
    if i-1 < 0:
        dp_1 = 0
    elif dp[i-1] == -1:
        dp_1 = 0
    else:
        dp_1 = dp[i-1]
    
    if i-2 < 0:
        dp_2 = 0
    
    elif dp[i-2] == -1:
        dp_2 = 0
    else:
        dp_2 = dp[i-2]
    
    dp[i] = dp_1 + dp_2
    

print(dp[-1] % (10**9 + 7))
    