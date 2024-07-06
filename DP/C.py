N = int(input())
playlist = []

for _ in range(N):
    playlist.append(list(map(int,(input().split(" ")))))

dp =[[0]* 3 for _ in range(N)]

dp[0] = playlist[0]

for i in range(1,N):
    dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + playlist[i][0]
    dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + playlist[i][1]
    dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + playlist[i][2]
    
print(max(dp[N-1]))