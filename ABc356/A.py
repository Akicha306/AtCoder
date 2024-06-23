N,L,R = list(map(int, input().split()))

answer =  [i for i in range(1, N+1)]
answer[L-1:R] = answer[L-1:R][::-1]

print(*answer)