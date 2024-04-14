N = int(input())
bits = N
answerList = []

for i in range(2**N):
    bitstr = f'{i:0{bits}b}' # Convert i to binary string with N bits
    
    leftBucketCount=0
    
    for index in range(0,len(bitstr)):
        if bitstr[index] == '1':
            leftBucketCount += 1
        else:
            leftBucketCount -= 1
            
        if leftBucketCount < 0:
            break
    
    if leftBucketCount == 0:
        answerList.append(bitstr.replace('1','(').replace('0',')'))


if(len(answerList)!=0):
    answerList.sort()
    for i in answerList:
        print(i)
