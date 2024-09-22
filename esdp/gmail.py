import re
pattern=re.compile(r'[A-Za-z0-9] +@+.+[a-z]')
text=input ("Enter email:")
match=re.fullmatch(pattern,text)
print(match)
if match:
    print("Email is valid")
else:
    print("email is not valid")


