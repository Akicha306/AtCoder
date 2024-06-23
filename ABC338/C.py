N,M,K = list(map(int,input().split()))
C = []

for i in range(K):
    C.append(list(map(int,input().split())))

for i in range(2**N):
    bin_i = bin(i)[2:]
    if bin_i.count('1') < K:
        continue
    
    if len(bin_i) < N:
        bin_i = '0'*(N-len(bin_i)) + bin_i
        
    for j in range(len(C)):
        