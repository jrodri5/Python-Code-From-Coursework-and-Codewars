'''
Created on 9/25/17
@author:   Justin Rodriguez
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. @jrodri5

CS115 - Hw 3
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def change(amount, coins):
    """Returns the amount of coins used to make change"""
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    if coins[0] > amount:
        return change(amount, coins[1:])
    use_it = 1 + change(amount - coins[0], coins)
    lose_it = change(amount, coins[1:])
    return  min(use_it, lose_it)

def giveChange(amount,coins):
    """Returns the amount of coins used to make change as well as the list of coins used."""
    if amount == 0:
        return [0, []]
    if coins == []:
        return [float("inf"), []]
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    else:
        use_it = giveChange(amount - coins[0], coins)
        use_it = [1 + use_it[0], use_it[1] + [coins[0]]]
        lose_it = giveChange(amount, coins[1:])
        if use_it[0] > lose_it[0]:
            return lose_it
        else:
            return use_it

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def letterScore(letter, scorelist):
    '''Takes as input a single letter string and a list, then returns the number value associated with the given letter.'''
    if scorelist == []:
        return []
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

def wordScore(n, scorelist):
    """Returns the scrabble score of the string."""
    return reduce(add,map(lambda x:letterScore(x, scorelist), n))

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    return [[dct[0],wordScore(dct[0],scores)]] + wordsWithScore(dct[1:],scores)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0 :
        return []
    elif n > len(L):
        return L
    return [L[0]] + take(n - 1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0: 
        return L[0:]
    if L == []:
        return []
    return drop(n-1, L[1:])


