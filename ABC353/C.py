N = int(input())
A = list(map(int, input().split()))
answer =0

for i in range(N):
    for j in range(i+1,N):
        answer +=(A[i]+A[j])%10**8

print(answer)