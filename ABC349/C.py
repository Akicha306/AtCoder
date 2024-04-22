S = input()
T = input()

def judgeShortstr(str, compareStr, judge):
    compareIndex = 0

    for i in range(len(str)):
        if str[i] == compareStr[compareIndex]:
            compareIndex += 1

        if compareIndex >= judge:
            return "Yes"

    return "No"

if T[-1] == 'X':
    print(judgeShortstr(S, T.lower(), 2))
    
else:
    print(judgeShortstr(S, T.lower(), 3))
    