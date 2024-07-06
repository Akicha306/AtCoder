string = input()
lowercase_count = 0
uppercase_count = 0

for char in string:
    if char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1

if lowercase_count >= uppercase_count:
    string = string.lower()
else:
    string = string.upper()
    
print(string)