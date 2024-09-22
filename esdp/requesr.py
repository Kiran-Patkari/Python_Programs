import re,urllib
import urllib.request
sites="google udemy".split()
print(sites)
for s in sites :
    print("Searching...",s)
    u=urllib.request.urlopen("https://"+s+".com")
    text=u.read()
    title=re.findall("<title>.*</title>",str(text),re.I)
    print(title[0])

    
    
    
