import re
#get user name from url 
#Solve 1: my user name is https://twitter.com/username 
#solve 2: https://twitter.com/username/

#method 1: replace
url = input('url:')
username =  url.replace("https://twitter.com/","")

#method 2 do not work solve 1
username = url.removeprefix('https://twitter.com/')

inp = input('enter twitter:')
#method 3 by sub but solve 1 remain
if matches:= re.search("^https?://(www\.)?twitter\.com/(.+)$",inp,re.IGNORECASE):
    print(matches.group(2))

#or usin (?:)
if matches:= re.search("^https?://(?:www\.)?twitter\.com/(.+)$",inp,re.IGNORECASE):
    print(matches.group(1))