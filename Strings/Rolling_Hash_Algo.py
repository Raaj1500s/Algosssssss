"""
Hashing algorithms are helpful in solving a lot of problems.

We want to solve the problem of comparing strings efficiently. 
The brute force way of doing so is just to compare the letters of both strings, 
which has a time complexity of O(min(n_1, n_2)) if n_1 and n_2 are the sizes of the two strings. We want to do better. 
The idea behind the string hashing is the following: 
    we map each string into an integer and compare those instead of the strings. 
    Doing this allows us to reduce the execution time of the string comparison to O(1).
    hash_val of string -> summation i = 0 to len(string) (string[i]*p power i) mod m
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

"""
Problem: Given two strings - a pattern 'P' and a text 'T', 
determine if the pattern appears in the text and if it does, enumerate all its occurrences in O(|P| + |T|) time.

Algorithm: Calculate the hash for the pattern P. 
Calculate hash values for all the prefixes of the text 'T'. Now, we can compare a substring of length |P| with 'P' 
in constant time using the calculated hashes. So, compare each substring of length |P| with the pattern. 
This will take a total of O(|T|) time. Hence the final complexity of the algorithm is O(|T| + |P|)
O(|P|) is required for calculating the hash of the pattern and
O(|T|) for comparing each substring of length |s| with the pattern.
"""


def stringMatch(P,T):
    prime = 31
    mod = 1000000009
    power = 1
    n = len(T)
    m = len(P)
    hash = [0]*(n+1)
    for i in range(n):
        hash[i+1] = (hash[i] + (ord(T[i]) - ord('a'))*power) % mod
        power *= prime % mod
    
    hash_pattern = 0
    power = 1
    for i in range(m):
        hash_pattern += ((ord(P[i]) - ord('a'))*power) % mod
        power *= prime % mod
    
    print(hash,hash_pattern)
    power = 1
    positions = []
    for i in range(0,n-m+1):
        curr_hash = (hash[i+m] - hash[i]) % mod
        if curr_hash == (hash_pattern * power) % mod:
            positions.append(i)
        power *= prime % mod
    

    return positions

print(stringMatch("abcd","abcdabcdabcd"))