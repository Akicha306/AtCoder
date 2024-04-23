N = int(input())
OutputStr=""

for i in range(1,N+1) :
    if i % 3 == 0:
        OutputStr += "x"
    else:
        OutputStr += "o"
        
print(OutputStr)