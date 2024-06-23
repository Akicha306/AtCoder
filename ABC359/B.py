N = int(input())

S = list(map(int, input().split(" ")))

list = [[0]*3 for _ in range(N)]
ans = 0

for i,value in enumerate(S):
    list[value-1][list[value-1][2]] = i
    list[value-1][2] += 1
    
for i in list:
    if abs(i[0] - i[1]) == 2:
        ans += 1

print(ans)
