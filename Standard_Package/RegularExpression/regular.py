import re

# if re.search(r"^[a-z0-9]+@[a-z0-9]+\.edu$",'aa@sdfg.edu'):
#     print('true')


if re.search('.','hh'):  #find the first char 'h' do not care others
    #True: a,b,c,'ab'.../ 
    #False: '', wihtout any char 
    print('true')

if re.search('.*',''):  #find the first char
    #True: a,b,c,'ab'.../ 
    #True: '', wihtout any char is ture (0/more)
    print('true')

if re.search('.+',''):  #find the first char
    #True: a,b,c,'ab'.../ 
    #False: '', wihtout any char is ture (0/more)
    print('true')

if re.search('.?','aaa'):  #find the first char
    #True: a,b,c,'ab'.../ 
    #False: '', wihtout any char is ture (0/more)
    print('true ?')

if re.search('[a-b]{3}','aaa'):  #abbcd => abbcd: match=abb,aaa,baa,...
    print('true ?')

if re.search('[a-b]{1,3}','aaa'):  #True: a=>a, aas=> aa,  
    print('true ?')

if re.search('^z\wP$','asP'):  #True: just zsP  
    print('true ?')


if re.search('^z\w*P$','asP'):  #True: z(any char with any len without space)P  
    print('true ?')

if re.search('^z\w*P$','asP'):  #False: asadfP, basdfasdfP, aorb(anyvhar)P  
    print('true ?')

if re.search('[a-z]','asP sdf'):  #search two text:asP, sdf
    print('true ?')

if re.search('[a-z] ','asP sdf'):  #search all text:asP sdf
    print('true ?')