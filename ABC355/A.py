A,B = list(map(int, input().split()))
human = [1,2,3]

if A in human:
    human.remove(A)

if B in human:
    human.remove(B)
    
if len(human) == 1:
    print(human[0])
else:
    print(-1)