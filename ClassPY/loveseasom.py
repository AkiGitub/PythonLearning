from datetime import date
import inflect
import re
import sys
import dateutil.parser as dateparser

p = inflect.engine()

class clsSeasonsLove:

    num2WordsEng = inflect.engine()

    def __init__(self,dateValue):
        #when declaring the class, get date from user
        #put it in property dataValue to check the calidity of date
        self.dateValue = dateValue
        self.__minDuration = ''

    @classmethod
    def getInput(cls):
        return input('Date of Birth:')

    def checkDateValidity(self):
        pattern = r'\d{4}-\d{1,2}-\d{1,2}'
        if re.search(pattern,self.__dateValue):
            self.calMinofDate() #calculate
        else:
            raise sys.exit('Invalid date')

    #get dutration of birth
    def cal_miutes(self):
        dtBirthDay = dateparser.parse(self.__dateValue)
        dtBirthDay =dtBirthDay.date()
        dtnow = date.today()
        dtnow = date(year=dtnow.year,month=dtnow.month,day=dtnow.day)

        dur = dtnow - dtBirthDay
        self.__dateValue = dur.days * 24 * 60

    def calMinofDate(self):
        self.cal_miutes()
        strConverted =self.num2WordsEng.number_to_words(self.__dateValue)
        #change first letter to upper case
        self.__dateValue = strConverted.lower().capitalize()
        #remove and with replace or regular expression
        self.__dateValue = re.sub(r"\b\sand\s\b",' ',
                    self.__dateValue)
        #add minutues
        self.__dateValue =self.__dateValue +' minutes'

    @property
    def dateValue(self):
        return self.__dateValue

    @dateValue.setter
    def dateValue(self,value):
        self.__dateValue = value
        self.checkDateValidity()

    #with print object access to converted variable
    def __str__(self):
        return self.__dateValue

def main():
     objSeasonLove = clsSeasonsLove(clsSeasonsLove.getInput())
     dd= str(objSeasonLove)
     print(dd)

if __name__ == "__main__":
    main()
