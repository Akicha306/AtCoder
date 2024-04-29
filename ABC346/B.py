S = "wbwbwwbwbwbw"*20
W,B = map(int,input().split())

for i in range(0,len(S)):
    w_count =0
    b_count =0
    
    for j in range(i,len(S)):
        if S[j] =="w":
            w_count +=1
        else:
            b_count +=1
            
        if w_count > W or b_count > B:
            break
        elif w_count == W and b_count == B:
            print("Yes")
            exit()
        else:
            continue

print("No")