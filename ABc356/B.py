N,M = list(map(int, input().split()))
A = list(map(int, input().split()))
sum = [0]*(M)

for i in range(N):
    X = list(map(int, input().split()))
    for j in range(M):
        sum[j] += X[j]
        
for i in range(M):
    if sum[i] < A[i]:
        print("No")
        exit()
    
print("Yes")