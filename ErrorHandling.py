def cal_facror(age):
    if age <=0:
        raise ValueError('age can not be zero or negative')
    return 10 / age

try:
    cal_facror(-1)
except ValueError as error:
    print(error)

#if do not have any exception
try:
    age= int(input('age:'))
except ValueError as ex:
    print('value in not valid')
    print(ex)
else:
    print('no exception excuted')


try:
    print(x)
except:
    print('error occured')

#Many Exceptions
try:
    print(x)
except NameError:
    print('the variable not defined')
except:
    print('Somethig else went wrong')

try:
    f= open('temp.py')
    try:
        f.write('writted tgrough the file')
    except:
        print('Error in writing file')
    finally:
        f.close()
except:
    print('Error in opening')


x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = 'hello'

if not type(x) is int:
    raise TypeError("Only integer ")

