
def grid_func(level:int):
    if level == 1:
        grid = [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]]
        return grid
    elif level == 0:
        return [["#"]]
    else:
        pre_grid = grid_func(level-1)
        
        size = len(pre_grid)
        grid = [["."]*(size*3) for _ in range(size*3)]
        
        for i in range(3):
            for j in range(3): 
                if i == 1 and j == 1:
                    continue
                x_location = j * size
                y_location = i * size
                
                for y in range(size):
                    for x in range(size):
                        grid[y_location + y][x_location + x] = pre_grid[y][x]
        return grid


N = int(input())
ans_list=grid_func(N)
2
for i in ans_list:
    print("".join(i))

