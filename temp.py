import inflect
from datetime import datetime
import re
import sys

p = inflect.engine()

def checkDateValidity(userDate):
        #pattern that use input is correct
        pattern = r'\d{4}-\d{1,2}-\d{1,2}'


        if re.search(pattern,userDate):
            dtBirthDay = datetime.strptime(userDate,'%Y-%m-%d')
            dtnow = datetime.today()
            dtnow = datetime(year=dtnow.year,month=dtnow.month,day=dtnow.day)

            dur = dtnow - dtBirthDay
            dateValueMin = int(dur.days * 24 * 60)
            
            strConverted =p.number_to_words(dateValueMin)
            #change first letter to upper case
            dateValueFirstUp= strConverted.lower().capitalize()
            #remove and with replace or regular expression
            dateValueFirstUp = re.sub(r"\sand\s",' ',dateValueFirstUp)
            #add minutues
            dateValueFirstUp =dateValueFirstUp +' minutes'
            print(dateValueFirstUp)
        else:
            raise sys.exit('Invalid date')

def main():

    #get user input
    userDate = input('Date of Birth: ')
    checkDateValidity(userDate)

if __name__ == "__main__":
    main()
