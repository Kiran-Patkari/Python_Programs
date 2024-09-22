#replace desired [pattern with specified pattern]

import re
pattern=r'[A-Za-a]+ions'
text="Lions spend much of A their times in resting"
match=re.sub(pattern,"A",text)
print(match)

#p=input("Enter pattern: ")
#t=input("Enter text: ")
#m=re.sub(p,"A",t)
#print(m)