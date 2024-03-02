N=int(input())
item = [list(map(int, input().split())) for i in range(N)]

W=int(input())

dp = [0 for i in range(W) for j in range(N)]

