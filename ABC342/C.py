N = int(input())
S = input()
Q = int(input())
dict = {}

for i in range(N):
    if S[i] not in dict:
        dict[S[i]] = []
    dict[S[i]].append(i)

for i in range(Q):
    c,d = input().split()
    if c not in dict:
        dict[c] = []
    if d not in dict:
        dict[d] = []
    
    if c==d:
        continue
    if dict[c]==[]:
        continue
    
    cList = dict[c]
    
    for j in cList:
        S = S[:j] + d + S[j+1:]
        dict[d].append(j)
    
    dict[c].clear()
    
print(S)
    
