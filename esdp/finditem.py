import re
pattern=r'[A-Za-a]+ions'
text="Lions spend much of their times in resting"
match=re.finditer(pattern,text)
for i in match:
  print(i)