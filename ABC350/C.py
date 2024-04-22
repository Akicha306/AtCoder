N = int(input())
A = list(map(int,input().split()))
Output = []

# 最初の解答例

def merge(threshold,list,realstart):
    start =0
    if len(list) <= 1:
        return
    
    for i in range(len(list)):
        if list[i]<= threshold:
            if start != i:
                temp = list[start]
                list[start] = list[i]
                list[i] = temp
                change = f'{start+realstart} {i+realstart}'
                Output.append(change)
                start += 1
    
    merge(int(threshold/2),list[:start],threshold)
    merge(int((threshold+1+N)/2),list[start:],)     
    
merge(int(N/2),A,1)       
print(len(Output))
for i in Output:
    print(i)   


