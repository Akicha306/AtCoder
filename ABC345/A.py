S = input()
flag = True
leftbracket_count = 0
rightbracket_count = 0

if S[0] == '<':
    for i in S:
        if i == '>':
            rightbracket_count += 1
        elif i == '<':
            leftbracket_count += 1

        if rightbracket_count > 0 and i == "=":
            flag = False
            break

else:
    flag = False

if rightbracket_count != 1 or leftbracket_count != 1:
    flag = False
    
print("Yes" if flag else "No")

