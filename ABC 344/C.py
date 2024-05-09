N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

combo = set()
for i in range(0, N):
    for j in range(0, M):
        for k in range(0, L):
            combo.add(A[i] + B[j] + C[k])


for i in X:
    if i in combo:
        print("Yes")
    else:
        print("No")
