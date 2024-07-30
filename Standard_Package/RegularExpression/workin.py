import re
import sys


def main():
    print(convert('12 AM to 12 PM'))


def convert24Hour(text,AMorPM):
    imin=iHoure24 = 0
    if ':' in text:
        spliteText= text.split(':')

        iHoure24 = int(spliteText[0])
        imin = int(spliteText[1])
        if (imin>=60):
            raise ValueError
    else:
        iHoure24 = int(text.strip())

    if AMorPM=='PM':
        iHoure24 = iHoure24 +12
        
    if (iHoure24>=24):
        iHoure24=12

    return [iHoure24,imin]


def convert(s):
    pattern = r"(\d{1,2}(?::\d{1,2})?)\s(AM|PM)\sto\s(\d{1,2}(?::\d{1,2})?)\s(AM|PM)"
    try:
        if matches:= re.search(pattern,s):

            ifirstHour,ifirstMin = convert24Hour(matches.group(1),matches.group(2))

            isecondHour,isecondMin = convert24Hour(matches.group(3),matches.group(4))
            
            if ifirstHour==12 and ifirstMin==0:
                if isecondHour==12 and isecondMin==0:
                    ifirstHour=ifirstMin=isecondMin=0
                    isecondHour=12


            return f"{ifirstHour:02}:{ifirstMin:02} to {isecondHour:02}:{isecondMin:02}"
        else:
            raise ValueError

    except ValueError:
        raise ValueError

if __name__ == "__main__":
    main()


    