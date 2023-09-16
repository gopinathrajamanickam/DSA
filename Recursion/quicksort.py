#!/usr/bin/env python3

def quickSort(array):
    # Handle the base case 
    if len(array) <= 1:
        return array
    return quickSort([x for x in array[1:] if x < array[0]]) \
           + [array[0]] \
           + quickSort([x for x in array[1:] if x >= array[0]])
    

if __name__ == '__main__':
    test_arr = [ [10,222,4243,1312,51,52342646,3,2,1]
                ,[1,2,1,3,5]
                ,[3,4,6,7,89,9]
                ,[1,2,34,5,3,2]
               ]
    for arr in test_arr:
        print(quickSort(arr))
    
    