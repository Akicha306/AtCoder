Q = int(input())
query = []
answer = []
for _ in range(Q):
    order,number = list(map(int, input().split()))
    if order == 1:
        query.append(number)
    elif order == 2:
        answer.append(query[-number])
        
for i in range(len(answer)):
    print(answer[i])
