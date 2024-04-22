S= input()

dictionary = {}
valueDictionary = {}

for i in S:
    dictionary[i] = dictionary.get(i,0)+1

for i,j in dictionary.items():
    valueDictionary[j] = valueDictionary.get(j,0)+1

for i,j in valueDictionary.items():
    if j != 2:
        print("No")
        exit()

print("Yes")