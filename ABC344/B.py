A=[]
for _ in range(0,100):
   A.append(int(input()))
   if A[-1]==0:
      break

A.reverse()

for i in A:
   print(i)