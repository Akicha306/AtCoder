import numpy as np

N= int(input())

A = int(np.power(N,1/3))
Output = ""
MaxValue = 0

if(np.power(A,3)==N) :
    MaxValue = N
else:
    MaxValue = A

for i in range(MaxValue, 0, -1):
    value = int(np.power(float(i),3))
    if(str(value) == ''.join(reversed(str(value)))) :
        Output = value
        break

print(Output)
