N = int(input())
A = list(map(int, input().split()))

B = []

for i,_ in enumerate(A[:-1:]):
    B.append(A[i]*A[i+1])

print(" ".join(map(str, B)))