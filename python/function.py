#def sample():
   # print('this is sample function')
    #return'thankyou'
#print(sample())


# def palindrome(x):
#     if isinstance(x,int):
#         print('logic for integer')
#     elif isinstance(x,str):
#         print('logic for string')
#     else:
        # print('only integers or strings is allowed')




def palindrome(x):
    if isinstance(x,int):
        print('logic for integer')
        rev=0
        temp=x
        while x>0:
            ld=x%10
            rev=rev*10+ld #0*10+3--->3,3*10+2==>32
            x=x//10
        if rev==temp:
            print('it is a palindrome')
        else:
            print('it is not a palindrome')
    elif isinstance(x,str):
        rev=""
        for char in range(len(x)-1,-1,-1):
            rev+=x[char]
        if rev==x:
            print('it is palindrome')
        else:
            print('it is not a palindrome')  
        #print('logic for string')
    else:
        print('only integers or strings is allowed')
        palindrome(121)
        palindrome('level')
        palindrome('markram')




def function():
    print('i am function 1')
function()