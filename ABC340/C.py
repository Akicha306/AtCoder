N = int(input())
memo = {}

def f(x):
    if x in memo:
        return memo[x]
    
    if x == 1:
        return 0
    else:
        memo[x] = f(int(x/2))+ f(x-int(x/2))+x
        return memo[x]
    
print(f(N))