import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
      try:
        #convert string to lowercase (Um, )
        s=s.lower()
        listofUM = re.findall(r'\bum\b',s)
        return len(listofUM)
      except ValueError:
          raise ValueError


if __name__ == "__main__":
    main()
