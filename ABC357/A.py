H,M = list(map(int, input().split()))
H=list(map(int, input().split()))

ans =0
for i in H:
    M-=i
    if M<0:
        break
    else:
        ans+=1
        
print(ans)