################################################################################
'''
Recursion 
3 steps to create a recursive function

    1. Find the base case 
    2. Find the recursive case and make sure to change input towards base case 
    3. Check the unintentional cases 

Name : gcd.py
Desc : To find the greatest common divisor for 2 or more numbers that divide 
       them without reminder 
'''
################################################################################

def gcd(a, b):
    # Euclidian Algorithm
    '''
    gcd(a,0) = a 
    gcd(a,b) = gcd(b, a%b)
    '''
   
    # Unintended case 
    '''
    Check if number is integer only
    if number is negative cosnider only absolute value of it 

    '''
    assert int(a) == a and int(b) == b, 'Input value should be a integer'
    a, b = abs(a), abs(b)
    
    # print("a : ",a)
    # print("b : ",b)

    # base case 
    if b == 0:
        return a 
    # recursive case 
    else:
        return gcd(b, a % b)


print(gcd(48,-18))

