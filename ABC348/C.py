N = int(input())
beans=[]
tasty_dict = {}

for i in range(N):
    beans.append(list(map(int,input().split())))


for i in beans:
    if(tasty_dict.get(i[1]) == None):
        tasty_dict[i[1]] = i[0]
    elif(tasty_dict.get(i[1]) > i[0]):
        tasty_dict[i[1]] = i[0]

max_tasty = 0

for list in tasty_dict.items():
    max_tasty = max(max_tasty, list[1])
    
print(max_tasty)