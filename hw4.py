'''
Created on Sep 30, 2017

@author: Justin Rodriguez

I pledge my honor that I have abided by the Stevens Honor System @jrodri5
'''
    
def pascal_helper(n):
    """returns the sum of 2 numbers to continue to the next row"""
    if 1 >= len(n):
        return []
    return [n[0]+n[1]]+pascal_helper(n[1:])

def pascal_row(n):
    """returns the nth row in pascal's triangle"""
    if n == 0:
        return [1]
    return [1]+pascal_helper(pascal_row(n-1))+[1]

def pascal_triangle(n):
    """ return the 0 to the nth row in the pascal's triangle"""
    if n == 0:
        return [pascal_row(0)]
    return pascal_triangle(n-1)+[pascal_row(n)]