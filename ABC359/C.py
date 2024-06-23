S = list(map(int, input().split(" ")))
T = list(map(int, input().split(" ")))

y_direction = 0
x_direction = 0
ans = 0

if S[1]>T[1]:
    y_direction = -1
elif S[1]<T[1]:
    y_direction = 1
else:
    y_direction = 0

if  S[0]>T[0]:
    x_direction = -1
elif S[0]<T[0]:
    x_direction = 1
else:
    x_direction = 0

if x_direction == 1 and abs(S[0])%2 == 0 and abs(S[1])%2 == 0:
    S[0] = S[0] + x_direction
elif x_direction == 1 and abs(S[0])%2 == 1 and abs(S[1])%2 == 1:
    S[0] = S[0] + x_direction
elif x_direction == -1 and abs(S[0])%2 == 1 and abs(S[1])%2 == 0:
    S[0] = S[0] + x_direction   
elif x_direction == -1 and abs(S[0])%2 == 0 and abs(S[1])%2 == 1:
    S[0] = S[0] + x_direction 


if abs(S[0]-T[0]) <= abs(S[1]-T[1]):
    ans += abs(S[1]-T[1])

elif abs(S[0]-T[0]) > abs(S[1]-T[1]):
    x_count = abs(S[0]-T[0])
    ans += abs(S[1]-T[1])
    x_count -= abs(S[1]-T[1])
    S[0]=S[0]+ans*x_direction
    
    if x_direction == 1 and abs(S[0])%2 == 0 and abs(S[1])%2 == 0:
        S[0] = S[0] + x_direction
        x_count -= 1
    elif x_direction == 1 and abs(S[0])%2 == 1 and abs(S[1])%2 == 1:
        S[0] = S[0] + x_direction
        x_count -= 1
    elif x_direction == -1 and abs(S[0])%2 == 1 and abs(S[1])%2 == 0:
        S[0] = S[0] + x_direction
        x_count -= 1   
    elif x_direction == -1 and abs(S[0])%2 == 0 and abs(S[1])%2 == 1:
        S[0] = S[0] + x_direction 
        x_count -= 1
        
    if x_count%2 == 0:
        ans += x_count/2
    elif x_count%2 == 1:
        ans += x_count/2 + 1
        

print(ans)    
