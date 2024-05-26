N,M=list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B 
C.sort()
answer = "No"

for i in range(0, len(C)-1):
    if C[i] in A and C[i+1] in A:
        answer = "Yes"

print(answer)