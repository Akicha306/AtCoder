N,K=map(int, input().split())

A=map(int, input().split())

B=[]

for i in A:
    if (i%K==0):
        B.append(int(i/K))

B.sort()

print(" ".join(map(str, B)))