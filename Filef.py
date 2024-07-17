try:
    with open('text.stxt') as file:
        print('opened File')
    age=int(input('age:'))
    xfactor = 10 / age
except (ValueError ,ZeroDivisionError,FileNotFoundError) as ex:
    print(ex)
else:
    print('no error exceptions')
