'''
Created on Sep 19, 2017

@author: Justin Rodriguez
I pledge my honor that I have abided by the Stevens Honor System @jrodri5
'''
import sys
from cs115 import map, reduce, filter


sys.setrecursionlimit(10000)

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

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

def wordScoreCombo(x, scorelist):
    """Returns wordScore list with the string """
    return [x,wordScore(x, scorelist)]

def explode(wordstring):
    """Returns a list of letters from a list or string"""
    if wordstring == []:
        return []
    if wordstring == '':
        return []
    return [wordstring[0]] + explode(wordstring[1:])

def attemptWord(Rack, Word):
    """Attempts to make a word from the rack."""
    def makeWord(n, w):
        if n == [] :
            return []
        if w == []:
            return []
        y = len(filter(lambda x: x == w[0], n))
        if 0 < y and y <= len(w):
            n.remove(w[0])
            return  ([w[0]] + makeWord(n,w[1:]))
        return []
    y = ''.join(makeWord(explode(Rack), explode(Word)))
    if y == Word:
        return y
    return ''

def isInDict(w,D):
    """Checks if a word is in the dictionary"""
    if D == []:
        return 'invalid'
    return filter(lambda x:x==w, D)

def getList(Rack, Dictionary):
    """Gets the list of words from the dictionary"""
    if Dictionary == []:
        return []
    return [attemptWord(Rack, Dictionary[0])]+getList(Rack, Dictionary[1:])

def scoreList(Rack):
    """Creates a list of the words that can be made from the Rack"""
    def score(lst):
        if lst == []:
            return []
        return [wordScoreCombo(lst[0], scrabbleScores)] + score(lst[1:])
    return score(filter(lambda x: x != '',getList(Rack, Dictionary)))

def which_is_higher(j,k):
    """Compares the score of two words."""
    if j[1] > k[1]:
        return j
    return k

def bestWord(Rack):
    """Determines what is the max score"""
    L = scoreList(Rack)
    if L == []:
        return ['',0]
    return reduce(which_is_higher,scoreList(Rack))