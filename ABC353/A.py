N = int(input())
H = list(map(int, input().split()))

firstbill = H[0]
answer = -1

for i in range(0, N):
    if firstbill <H[i]:
        answer = i+1
        break
    
print(answer)