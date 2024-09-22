import re
pattern="hello"
text="hello this is kiran"
val=re.match(pattern,text)
print(val)

p=input("Enter your pattern:")
t=input("Enter your text:")
v=re.match(p,t)
print(v)