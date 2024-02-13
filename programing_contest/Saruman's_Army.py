N = int(input())
R = int(input())
X = [int(a) for a in input().split()]

point = 0

while X != []:
    left = X[0]
    left_limit = X[1]-R
    
    if(X[0]<left_limit):
        point += 2
        
    else:
        point+=1

    if(len(X)<3):
        X.pop()
        X.pop()
        break

    right = X[2]
    right_limit = X[1]+R

    if(right_limit<X[2]):
        for _ in range(3):
            X.pop()
    else: 
        for _ in range(2):
            X.pop()

print(point)

