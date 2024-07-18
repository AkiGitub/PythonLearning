import json
from pathlib import Path

# movies = [
#     {"id":1,"title":"Zogo","year":1983},
#     {"id":2,"title":"Aki","year":1985}
# ]

# data = json.dumps(movies)
# print(data) #the result is the same

# Path("d:\\temp\\jsFile.json").write_text(data)

data = Path('d:\\temp\\jsFile.json').read_text()
movies = json.loads(data)
print(movies) #