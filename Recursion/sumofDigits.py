################################################################################
'''
Name : sumOfDigits.py
Purpose : Function to get the sum of digits of a positive integer number 
'''

################################################################################

import sys 
sys.setrecursionlimit(10000)

def sumOfDigits(n):
    assert n >=0 and int(n) == n, 'Provide a positive integer '

    if n == 0:
        return 0
    else:
        return n%10 + sumOfDigits(n//10) 

print(sumOfDigits(1))
print(sumOfDigits(15))     
print(sumOfDigits(155))      