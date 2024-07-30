import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    pattern = r'src="(?:https?://)?(?:www\.)?youtube\.com/embed/(\w*)'
    if matches:= re.search(pattern,s):
        return 'https://youtu.be/'+ matches.group(1)
    
    return None
        


if __name__ == "__main__":
    main()
