# https://atcoder.jp/contests/dp/tasks/dp_a
N = int(input())
H = list(map(int, input().split()))

dp = [-1 for _ in range(N)]
dp[0] = 0

for i in range(1,N):
    h_1,h_2 = 10**9,10**9   
    if i-1 >= 0:
        h_1 = dp[i-1] + abs(H[i] - H[i-1])
    else :
        h_1 = 10**9
    
    if i-2 >= 0:
        h_2 = dp[i-2] + abs(H[i] - H[i-2])
    else:
        h_2 = 10**9
    
    dp[i] = min(h_1,h_2)

print(dp[-1])
        