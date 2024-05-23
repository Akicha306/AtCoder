N = int(input())
A = list(map(int, input().split()))

for i in range(0, N-1):
    S, T = list(map(int, input().split()))
    X = int(A[i]/S)
    Y = X*T
    A[i+1] += Y

print(A[-1])