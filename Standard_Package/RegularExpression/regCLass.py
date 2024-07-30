import re

name = input('name:').strip()

#() for capture we want from the text
matches=re.search(r"^(.+), (.+)$",name)

if matches:
    first,last  = matches.groups() #group(1) , group(2)
    name = f"{first}  {last}"
    print(f" {name}")

#solve space proble, with ? or *
matches=re.search(r"^(.+), ?(.+)$",name)

if matches:
    first,last  = matches.groups() #group(1) , group(2)
    name = f"{first}  {last}"
    print(f"with ?: {name}")

#:=
if matches:=re.search(r"^(.+), ?(.+)$",name):
    first,last  = matches.groups() #group(1) , group(2)
    name = f"{first}  {last}"
    print(f"with ?: {name}")