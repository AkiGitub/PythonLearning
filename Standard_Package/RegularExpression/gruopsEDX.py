import re

locations = {"+1":"United state and canada","+62":"Indonesia","+98":"Iran","+505":'nicaracoge'}

pattern = r"(?P<codeCountry>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
number = input('number:')

if match:= re.search(pattern,number):
    print('valid',locations[match.group('codeCountry')])

else:
    print('Invalid')

  