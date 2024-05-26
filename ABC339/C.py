N =input()
A = list(map(int, input().split()))
answer = 0

for i in A:
    answer += i
    if answer <0:
        answer = 0
    
print(answer)