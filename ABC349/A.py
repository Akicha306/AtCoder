N = int(input())
A = list(map(int,input().split()))
total = 0

for i in A:
    total += i
    
if total > 0:
    print(f'-{str(total)}')
else:
    print(str(abs(total)))
    