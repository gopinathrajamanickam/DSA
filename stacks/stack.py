"""
Created date : 29 Aug 2023
Author : Gopinath Rajamanickam
Program : Stack.py
Purpose : Implementation of Stack data structure in python

"""
class Stack:
    def __init__(self): # constructor 
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
        # return self.items 
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    # This is called when the stack object is passed to a print function
    def __str__(self): 
        return str(self.items)
    

if __name__ == "__main__":
    print("Hello")
    pass 
    s = Stack() # call the constructor 
    print(s)
    print(s.is_empty())
    
    s.push(3)
    print(f"After pushing 3  : {s}")

    s.push(7)
    print(f"After pushing 7  : {s}")
    
    s.push(5)
    print(f"After pushing 5  : {s}") 

    print(f"Size of the stack {s.size()}")
    
    print(s.pop())
    print(s)
    print(f"Size after pop {s.size()}")
    
    print(s.peek())
    print(s)
    print(f"Size after peek {s.size()}")