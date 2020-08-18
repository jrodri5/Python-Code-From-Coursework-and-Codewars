'''
Created on Jul 6, 2020

@author: Justin
'''


def isPrime(n):
    """Returns true if a number is prime and false if it is not"""
    if isinstance(n, float) == True:
        return "Not a whole number, try again"
    elif 0 <= n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True 

def divisibleBy(n):
    "returns a list of all numbers that number is divisible by"
    divisibles = []
    number = 1
    if isPrime(n) == True:
        return str(n) + " and 1"
    while number < n:
        if n % number == 0 and isPrime(number) == True:
            divisibles.append(number)
            number += 1
        else:
            number += 1
    return divisibles

def binToNum(s):
    """Returns the decimal value of the inputed binary string"""
    n = 7
    total = 0
    for i in s:
        total += int(i) * 2**n
        n -= 1
    return total

def prime(n):
    """If the number is prime it returns a string saying it is prime. 
    If not,will say it is not and return a list of all the numbers it 
    is divisible by."""
    if isPrime(n):
        return ("Yes! %d is a prime number!" % n)
    lst = divisibleBy(n)
    return ("No, %d is divisible by %s" % (n, lst))

print(prime(56))
    
