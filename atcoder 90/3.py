N = int(input())
roads = []


for i in range(N-1):
    roads.append(list(map(int, input().split())))

node = [[0] for _ in range(N)]
nodeFlag = [0 for _ in range(N)]

for i in range(roads):
    node[roads[i][0]].append(roads[i][1])


def dfs(v, p, endList):
    
    endinfo = [v, p]
    if nodeFlag[v] != 1:
        endList.append(v)
    return
    
    for i in range(node[v]):
            p += 1
            dfs(node[i][1])
    return


nodeFlag = [0 for _ in range(nodeFlag)]
endList = []

dfs(roads[i][0], 0, endList)
nodeFlag.clear()
dfs()

endList.sort(reverse=True)
