N,Q = map(int,input().split())
T = [1]*N

TreatList = map(int,input().split())

for i in TreatList:
    if(T[i-1]==0):
        T[i-1]=1
    else:
        T[i-1]=0
        
print(T.count(1))
