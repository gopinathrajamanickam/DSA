################################################################################
'''
Recursion 
3 steps to create a recursive function

    1. Find the base case 
    2. Find the recursive case and make sure to change input towards base case 
    3. Check the unintentional cases 

'''
################################################################################
import sys
sys.setrecursionlimit(10000)

def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer only!' 

    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(1.5))


