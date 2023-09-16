################################################################################
'''
Name : powerBy
Purpose : Function to get the exponential value for a value for an value. 

'''
################################################################################

import sys 
print("Current value of recursion limit is",sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print("Setting the recursion limit as ",sys.getrecursionlimit())
print(sys.__dict__)

def power(base, expo):
    
    # Unintented cases 
    assert expo>=0 and int(expo) == expo, 'Exponential component should be positive integer'

    # base condition
    if expo == 0:
        return 1

    if expo == 1:
        return base

    # Recursive call 
    return base * power(base, expo-1)

print(power(2,44))
print(power(1,0))
print(power(3.2,-2))


