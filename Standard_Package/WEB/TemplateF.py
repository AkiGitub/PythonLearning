from string import Template
from pathlib import Path
import os

print( os.getcwd())
print(__file__ + "\n")

fileHtml = os.path.dirname(Path(__file__))

temp = Template(Path(fileHtml+'\\'+'template.html').read_text())


print(temp.substitute({'user':'aki'}))

