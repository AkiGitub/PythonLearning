import os
from pathlib import Path

cwd = os.getcwd()
#print(cwd)

folder = cwd
subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]
#print(subfolders)

folder= Path(r'D:\temp\New folder')
[print(x) for x in os.walk(folder)]
   
#current foder with .
print("==>",next(os.walk('.'))[1])

#
print("==>",next(os.walk(folder))[1])