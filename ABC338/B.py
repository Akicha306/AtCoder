S = input()
dict = {}

for i in S:
    dict[i] = dict.get(i, 0) + 1

sorted_dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
print(sorted_dict[0][0])
