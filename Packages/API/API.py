#https://countrylayer.com/documentation/
import requests

url = 'https://holidayapi.ir/jalali/1401/11/22'

res = requests.get(url)

print(res.content)