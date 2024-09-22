import re
pattern=r'\d'
text="Hello 2,1,3 world"
match=re.search(pattern,text)
if match:
    print("Found",match.group)
else:
    print("Not Found")


p=input("Enter pattern")
t=input("Enter text:")
m=re.search(p,t)
if m:
    print("Found",match.group)
else:
    print("Not Found")