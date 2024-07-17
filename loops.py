
for i in range(9):
    print('')
    for j in range(i):
        print('*',end='')
#else cluase for --------------------------------------
  #break
  #A for or while loop can include an else clause.
  #In a for loop, the else clause is executed after the loop reaches its final iteration
  #In a while loop, it’s executed after the loop’s condition becomes false.
  #In either kind of loop, the else clause is not executed if the loop was terminated by a break.

for n in range(2,10):
    for x in range(2,n): #(2,n-1)
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else: #not active by break, end of the loop
        print(n,'is a prime number')

#continue--------------------------------------------
for num in range(2,10):
    if num % 2==0:
       print(num,'is Even')
       continue
    print(num,'is odd')

#for tamriniog--------------------------------------
list2= ['Zogo: '+str(x) for x in range(5)]
print(list2)#['Zogo: 0', 'Zogo: 1', 'Zogo: 2', 'Zogo: 3', 'Zogo: 4']

    