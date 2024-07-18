from pathlib import Path
from zipfile import ZipFile

# #create zip file
# zip = ZipFile(r"d:\temp\zipFile.zip","w")

# Files= Path(r"d:\nodejs").rglob("*.*")
# for p in Files:
#     zip.write(p)

#with, we do not need close 
with ZipFile(r"d:\temp\zipFile.zip") as zip:
     #print(zip.namelist())
     info = zip.getinfo("nodejs/package.json")
     print(info) #<ZipInfo filename='nodejs/package.json' filemode='-rw-rw-rw-' file_size=58>
     print(info.file_size)
     print(info.compress_size)
     #extract files of zip file
     zip.extractall(r"D:\temp\nn")
     