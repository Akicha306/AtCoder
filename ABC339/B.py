H,W,N = list(map(int, input().split()))

field = [["."]*W for _ in range(H) ]
x,y = 0,0
direction = 0

direction_list = [(0,-1),(1,0),(0,1),(-1,0)] 

while N > 0:
    if field[y][x] == ".":
        field[y][x] = "#"
        direction += 1
        if direction > 3:
            direction = 0
        
    else:
        field[y][x] = "."
        direction -= 1
        if direction < 0:
            direction = 3
    
    x,y = x + direction_list[direction][0], y + direction_list[direction][1]
    
    if x < 0:
        x = W- 1
    elif x >= W:
        x = 0
        
    if y < 0:
        y = H - 1
    elif y >= H:
        y = 0
        
    N -= 1
    
for i in range(H):
    print("".join(field[i]))
