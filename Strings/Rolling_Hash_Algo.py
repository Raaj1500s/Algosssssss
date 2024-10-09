"""
Hashing algorithms are helpful in solving a lot of problems.

We want to solve the problem of comparing strings efficiently. 
The brute force way of doing so is just to compare the letters of both strings, 
which has a time complexity of O(min(n_1, n_2)) if n_1 and n_2 are the sizes of the two strings. We want to do better. 
The idea behind the string hashing is the following: 
    we map each string into an integer and compare those instead of the strings. 
    Doing this allows us to reduce the execution time of the string comparison to O(1).
"""


def stringHash(string):
    p = 31
    m = 1e9 + 9
    hashcode = 0
    pow = 1
    for ch in string:
        hashcode += ((ord(ch)-ord('a')+1) * pow)%m
        pow = (pow*p) % m
    
    return hashcode

