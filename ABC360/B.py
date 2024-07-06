S,T = list(map(str,input().split()))



for i in range(1,len(S)):
    str = S
    splitStr = []
    
    while len(str) != 0:
        if len(str) < i:
            splitStr.append(str)
            str = ''
        else:    
            splitStr.append(str[:i])
            str = str[i:] 
     
    for c in range(1,i+1):
        allStr = ''
        for j in range(len(splitStr)):
            if len(splitStr[j]) >= c:
                allStr += splitStr[j][c-1]
        
        if allStr == T:
            print('Yes')
            exit()

print('No')
