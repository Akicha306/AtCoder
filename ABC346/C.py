N, K = map(int, input().split())
A = list(map(int, input().split()))
S = set(A)
ans = K*(K+1)//2
for i in S:
    if i <= K:
        ans -= i
print(ans)
