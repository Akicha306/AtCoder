N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

box = [[] for _ in range(N)]
answer = 0
for i,a in enumerate(A):
    if box[a-1] == []:
        box[a-1].append(W[i])
    else:
        if box[a-1][-1] > W[i]:
            temp = box[a-1].pop(-1)
            box[a-1].append(W[i])
            box[a-1].append(temp)
        else:
            box[a-1].append(W[i])  
            
for i in range(len(box)):
    if box[i] != []:
        answer += sum(box[i][:-1])
        
print(answer)