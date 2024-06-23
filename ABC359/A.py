N = int(input())
S = []
ans = 0

for i in range(N):
    S.append(input())
    
for i in S:
    if i[0] == "T":
        ans += 1

print(ans)