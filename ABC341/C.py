# オーダーがH*W*Nになりそうで500^3=125*10^6なのできつそうだが、ひとまず深さ探索で実装してみる

H, W, N = list(map(int, input().split()))
T = input()
S=[]
answer = []

for i in range(H):
    S.append(input())
        
def depth(x,y,root):
    if len(root)==0:
        answer.append((x+1,y+1))
        return "OK"
    
    first = root[0]
    root = root[1:]
    
    if first == "U":
        y -= 1
    elif first == "D":
        y += 1
    elif first == "L":
        x -= 1
    elif first == "R":
        x += 1
    else:
        print("error")
        return
    
    if y < 0 or y >= H or x < 0 or x >= W:
        return
    
    if S[y][x] == "#":
        return 
    else:
        return depth(x,y,root)
        
for i in range(W):
    for j in range(H):
        if S[j][i] == "#":
            continue
        
        result=depth(i,j,T)
        # if result == "OK":
        #     print((i+1,j+1))
        
# print(answer)
print(len(answer))