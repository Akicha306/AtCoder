N = int(input())

A = int(N**(1/3))
Output = ""
MaxValue = A

for i in range(MaxValue+1, 0, -1):
    if (n := i**3) > N:
        continue
    value = str(i**3)
    if (value == value[::-1]):
        Output = value
        break

print(Output)
