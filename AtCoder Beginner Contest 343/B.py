N = int(input())
Graph = []
Output = []

for _ in range(N):
    line = list(map(int, input().split()))
    Graph.append(line)

for i in range(N):
    connect = []

    for j in range(len(Graph[i])):
        if Graph[i][j] == 1:
            connect.append(str(j+1))

    Output.append(connect)

for i in range(len(Output)):
    pri = " ".join(Output[i])
    print(pri)
