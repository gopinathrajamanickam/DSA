"""
Created date : 29 Aug 2023
Author : Gopinath Rajamanickam
Program : stack_reverse_string.py
Purpose : Reverse a string 

"""
import stack

"""
This function accepts a sentence and prints its value in reverse
"""


def reverse_string(word: str) -> str:
    s = stack.Stack()
    for chr in word:
        s.push(chr)

    reversed_string = ""
    print(f"Given string is {s} is empty : {s.is_empty()}")

    while not s.is_empty():
        reversed_string += s.pop()

    return reversed_string
    # print(f"Reversed String is {reversed_string}")


if __name__ == "__main__":
    result = reverse_string("uoy llet I did tahw")
    print(result)
