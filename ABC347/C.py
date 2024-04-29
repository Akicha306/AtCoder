N,A,B= map(int, input().split())
D = list(map(int, input().split()))

all = A+B
changedList = list(map(lambda x: x%all, D))

my_list = [all if x == 0 else x for x in changedList]
my_list.sort(reverse=True)

for i in my_list:
    if i > A:
        print("No")
        exit()

print("Yes")