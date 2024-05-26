N,T = list(map(int, input().split()))

A = list(map(int, input().split()))
bingo_width = [0]*N
bingo_height = [0]*N
bingo_diagonal_left = 0
bingo_diagonal_right =0
answer = -1

for i in range(0,T):
    if A[i]%N == 0:
        width = N-1
        height = int(A[i]/N)-1
    else:
        width = (A[i]%N)-1
        height = int(A[i]/N)
    
    bingo_width[width] += 1
    bingo_height[height] += 1
    
    if width == height:
        bingo_diagonal_left += 1
        
    if width + height == N-1:
        bingo_diagonal_right += 1
        
    if bingo_width[width] == N or bingo_height[height] == N or bingo_diagonal_left == N or bingo_diagonal_right == N:
        answer = i+1
        break

print(answer)


