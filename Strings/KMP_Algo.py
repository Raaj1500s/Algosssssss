"""
You are given a string s of length n.The prefix function for this string is defined as an array "p" of length n,where
p[i] is the length of the longest proper prefix of the substring s[0......i] which is also a suffix of this substring. 
A proper prefix of a string is a prefix that is not equal to the string itself. By definition, p[0] = 0.
Mathematically the definition of the prefix function can be written as follows:
    pi[i] = k {max {k = 0.....i} {k : s[0.....k-1] = s[i-(k-1).....i]}}

"""

def prefixFunction(string):
    n = len(string)
    p = [0]*n
    for i in range(1,n):
        j = p[i-1]
        while j > 0 and string[i] != string[j]:
            j = p[j-1]
        
        if string[i] == string[j]:
            j += 1

        p[i] = j
    
    return p

print(prefixFunction("aabxaabxcaabxaabxay"))