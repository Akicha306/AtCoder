N = int(input())
all_list = []
answer_list = []

for i in range(0,N):
    number_list = list(map(int,input().split()))
    number_list.append(i+1)
    all_list.append(number_list)
    
all_list.sort(key=lambda x: x[1])

if all_list[0][0] < all_list[1][0]:
    answer_list.append(all_list[0][2])
    
for i in range(1,N):
    if all_list[i-1][0] > all_list[i][0]:
        continue
    
    answer_list.append(all_list[i][2])



answer_list.sort()
print(len(answer_list))
print(' '.join(map(str,answer_list)))