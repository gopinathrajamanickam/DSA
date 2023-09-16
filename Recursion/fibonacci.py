################################################################################
'''
Name : Fibonacci
Purpose : Function to get the fibonacci value for a specific index. 
          it starts with 0,1,1,2,3,5
'''

################################################################################

import sys 
sys.setrecursionlimit(1000)

def fibonacci(n):
    
    # Unintentional case 
    assert n>=0 and int(n) == n, ' The index should be a positive integer'

    # base case 
    if n in [0,1]:
        return 1
    # recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))  
print(fibonacci(10))    
print(fibonacci(1.5))     
