from bisect import bisect_left

N=int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()

answer = []

for i in range(Q):
    B = int(input())
    
    position = bisect_left(A, B)
    
    if position == 0:
        answer.append(abs(A[position] - B))
    elif position == N:
        answer.append(abs(A[position-1] - B))
    else:
        answer.append(min(abs(A[position] - B), abs(A[position-1] - B)))
        
for i in answer:
    print(i)