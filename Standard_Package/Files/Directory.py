from pathlib import Path
from time import ctime 
 
path = Path(r"D:\Learning\tamrin\zogo2")

# if path.exists():
#     print("ISExist")
#     path.rename("zogo2") #
#    # path.rmdir()
# else:
#     path.mkdir()
    
# print(path)

#this method for millions of files makes memery full
# for p in path.iterdir():
#     print(p)
    
#to solve about issues: list comprehension expresion
paths= [ p for p in path.iterdir() if p.is_dir()]  #PosixPath / WindowsPath
print(paths) #[WindowsPath('D:/Learning/tamrin/zogo2/New folder'), WindowsPath('D:/Learning/tamrin/zogo2/New folder (2)')]

pyFiles= [p for p in path.glob('*.py')]
print(pyFiles) #[WindowsPath('D:/Learning/tamrin/zogo2/New Text Document - Copy.py'), WindowsPath('D:/Learning/tamrin/zogo2/New Text Document.py')]

#for subFolders --------------------------------
pyFilesSubFolders = [p for p in path.rglob('*.py')]
print(pyFilesSubFolders) #[WindowsPath('D:/Learning/tamrin/zogo2/New Text Document - Copy.py'), WindowsPath('D:/Learning/tamrin/zogo2/New Text Document.py'), WindowsPath('D:/Learning/tamrin/zogo2/New folder/zzz.py')]

#Files =======================================================
path = Path(r"D:\Learning\tamrin\zogo2\New folder\zzz.py")
if (path.exists):
    print('file existed')
    #path.rename('zogo2.py')
    #path.unlink()  #remove the selected file

print(path.stat())  #inforation of file
#os.stat_result(st_mode=33206, st_ino=2533274790588497, st_dev=15344492446873975558, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1721230899, st_mtime=1721230899, st_ctime=1721230899)

#creattion time
print(ctime(path.stat().st_ctime)) #Wed Jul 17 19:11:39 2024

#read bytes
str1=path.read_text()
print(str1) #sdsdf

#anothre way
with open(r"D:\Learning\tamrin\zogo2\New folder\zzz.py","r") as file:
     print(file.readlines()) #['sdsdf']
     file.close()

path.write_text('zzzz') #remove old data

import shutil 
#method copy file
target = Path(r'D:\Learning\tamrin\zogo2\New folder\zogonew.txt')

shutil.copy(path,target)
#to write need file
target.write_text(path.read_text())

#---------