import re
pattern=r'\W'
text="Lions spend much of their times in resting"
match=re.split(pattern,text)
print(match)

p=input("Enter pattern: ")
t=input("Enter text: ")
m=re.split(p,t)
print(m)