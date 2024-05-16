N = int(input())
P = list(map(int, input().split()))
Q = int(input())
answer =[]

for i in range(Q):
    A, B = map(int, input().split())
    A_index = P.index(A)
    B_index = P.index(B)
    
    if(A_index < B_index):
        answer.append(A)
    else:
        answer.append(B)
        
for a in answer:
    print(a)

        

