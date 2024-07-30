import re

#1 check rules: #start, 6 chars (0-9A-F)
inp = input('HEx:')

pat = r"#[a-fA-F0-9]{6}$"
if match :=re.search(pat,inp):
    print(match.group())
