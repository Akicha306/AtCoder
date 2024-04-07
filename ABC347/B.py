S = input()

all = []

for i in range (1,len(S)+1):
    firstPoint = i-1
    
    for j in range(0,len(S)-firstPoint):
        
        part = S[j:j+i]
        
        isExistPart = False
        
        for k in all:
            if k == part:
                isExistPart = True
                break
        
        if isExistPart == False:
            all.append(part)
            
print(len(all))
        
            
        
        



        