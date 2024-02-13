N = int(input())
X = [int(input()) for _ in range(N)]

X.sort(reverse=True)
total =0

while len(X) > 1:
    total += sum(X)
    X.pop(0)

print(total)