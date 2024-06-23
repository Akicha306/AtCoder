n = int(input("Enter the number of entries: "))
dict_list = []

for _ in range(n):
    x, y = map(int, input().split())
    dict_list.append({'x_key':x, 'y_key':y})
print(dict_list)