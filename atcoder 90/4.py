h,w = map(int(),input().split())

b=[]

for _ in range(0,h):
    c= list(map(int,input().split()))
    b.append(c)

b_row = [0 for _ in range(0,w)]
b_column= [0 for _ in range(0,h)]

for i in range(0,h):
    for j in range(0,w):
        b_row[j] += b[i][j]
        b_column[i] += b[i][j]

