listMonths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

textError = 'Error'

def Date2NumericDate(strDate):
     
    #split date to year, month, day
    splitedDate = strDate.split('/') 
    if len(splitedDate) == 3:
       month = splitedDate[0]
       day =   splitedDate[1]
       year =  splitedDate[2]

       if (not month.isnumeric()):
           return textError
       
       if (int(month) > 12):
           return textError
       
       if (int(day) > 31):
           return textError

       return [int(year),int(month),int(day)]
    else:
        return textError

def Date2TextDate(strDate):
    #remove , from date to split it
    strDate=strDate.replace(',','')
    #split date to year, month, day
    splitedDate = strDate.split(' ')
    if len(splitedDate) == 3:
       month = splitedDate[0].lower().title()
       day = splitedDate[1]
       year = splitedDate[2]
       if not (month in listMonths):
           return textError
       
       if (int(day) > 31):
           return textError
       
       #convert  text month to number month
       month = listMonths.index(month) +1 
       return [int(year),int(month),int(day)]
    else:
        #if wrong date
        return textError
           
def main():
    #print(Date2TextDate('December 1, 1970'))
    while True:
        userDate = input('Date:')
        
        userDate= userDate.strip

        if  '/' in userDate:
            retDate = Date2NumericDate(userDate)
            if not 'Error' in retDate:
                print("{:04}-{:02}-{:02}".format(retDate[0],retDate[1],retDate[2]))
                break

        elif ',' in userDate:
            retDate = Date2TextDate(userDate)
            if not 'Error' in retDate:
                print("{:04}-{:02}-{:02}".format(retDate[0],retDate[1],retDate[2]))
                break
     
main()


