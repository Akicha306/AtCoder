S = input()

r_location=0
m_location=0


for i in range(len(S)):
    if S[i] == 'R':
        r_location = i
    elif S[i] == 'M':
        m_location = i

if r_location > m_location:
    print('No')
else:
    print('Yes')
    
