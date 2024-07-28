from calSquare import square

#basic methid to test
def testSquare():
    if square(2) != 4:
        print("error ")
    if square(3) != 9:
        print("error ")

#with Assert
def testSquare():
    try:
      assert square(2) == 4
    except:
      print('error in 2')
    
    try:
      assert square(3) == 9 #AssertionError
    except:
       print('Error 3')
    
    try:
      assert square(-1) == 1 #AssertionError
    except:
       print('Error -1')

#use by pytest

testSquare()