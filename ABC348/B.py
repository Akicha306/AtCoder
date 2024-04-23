N =int(input())
point=[]
distances=[[0]*N for _ in range(N)]

for i in range(N):
    point.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if i==j:
            distances[i][j]=0
        else:
            distances[i][j]=(((point[i][0]-point[j][0])**2)+((point[i][1]-point[j][1])**2))**(1/2)
            
for i in range(len(distances)):
    max = 0
    max_index =0
    for j in range(len(distances[i])):
        if distances[i][j]>max:
            max = distances[i][j]
            max_index = j
    print(max_index+1)

