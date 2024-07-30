import re
import sys


def main():
    for i in range(0,4):
        print(f'{i}.{i}.{i}.{i}')
    print(validate(input("IPv4 Address: ")))


#find the invalid ips
def checkIpItmes(listItmesIp):
    for item in listItmesIp:
        Iitem= int(item)
        if  Iitem<0 or Iitem>255: 
            return False
    return True

def validate(ip):
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    if matches:=re.search(pattern,ip):
        return checkIpItmes([matches.group(1),matches.group(2),matches.group(3),matches.group(4)])
    return False

if __name__ == "__main__":
    main()
