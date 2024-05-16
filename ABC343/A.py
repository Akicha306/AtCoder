A, B = map(int, input().split())

X = A + B

Y = [i for i in range(0, 10)]
Y.remove(X)

print(Y[0])