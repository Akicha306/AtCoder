N = int(input())

name_list = []
for _ in range(N):
    member_info = list(input().split())
    member_info[1] = int(member_info[1])
    name_list.append(member_info)

name_list.sort(key=lambda x: x[0])

total = sum([x[1] for x in name_list])

print(name_list[total%N][0])
