from pathlib import Path

path = Path(r'D:\Pasco')

for p in path.iterdir():
    print(p)