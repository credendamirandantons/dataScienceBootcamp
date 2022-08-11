def game(i):

    '''
    Objective
    Function determine the number based on the number 15
    
    Arguments:
    - i = a number, type integer
    - metode = (default), 
        expected values: [smal, greater]
    '''

# put unsafe operation in try block
try:
    print("A")
    
    # unsafe operation perform
    print(1 / 0) 
    
    #get type param first
    if (i < 15): #conditional statement
        result  = "i is smaller than 15"
    else:
        result  = "i is greater than 15"
        
# if error occur the it goes in except block
except:
    print("Muncul Error")
# final code in finally block
finally:
    print("Finish!")
    
    
    return result




