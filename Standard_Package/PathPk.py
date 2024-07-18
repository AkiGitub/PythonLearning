from pathlib import Path

#print(Path()) #"d:/Learning Docs/EDX/Code/Lecture1/PythonLeaning/Standard_Package/PathPk.py"
print(Path.home()) #C:\Users\pc

#check is exist the file
path = Path(r"D:\Learning Docs\EDX\Code\Lecture1\PythonLeaning\array.py")

print(path) #d:\IT STAFF.pdf
if path.exists(): #true
    print("is Exist Folder")

#check is file or directory
print(path.is_dir()) #false
print(path.is_file()) #true
print("==>",path.name) #IT STAFF.pdf  or folder name 
print(path.stem) #file name without extenction
print(path.suffix) #extenction
print(path.parent) #parent of selected folder

#file paht with new of it, without chaing it, ;ike template
path = path.with_name("temp.txt")  #path of file
print(path)#D:\Learning Docs\EDX\Code\Lecture1\PythonLeaning\temp.txt

path = path.with_suffix(".txt")  #path of file
print(path)#D:\Learning Docs\EDX\Code\Lecture1\PythonLeaning\temp.txt