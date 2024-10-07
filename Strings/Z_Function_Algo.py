'''
Suppose we are given a string "s" of length "n". The Z-function for this string is an array of length "n" where the
i-th element is equal to the greatest number of characters starting from the position
i that coincide with the first characters of "s"
In other words,
z[i] is the length of the longest string that is, at the same time, a prefix of
"s" and a prefix of the suffix of "s" starting at "i"
'''


def get_Z_Func(string):
    n = len(string)
    z = [0]*n
    l,r = 0,0
    for i in range(1,n):
        if i < r:
            z[i] = min(r-i, z[i-l])
        
        while z[i] + i < n and string[z[i]+i] == string[z[i]]:
            z[i] += 1
        
        if i + z[i] > r:
            r = i + z[i]
            l = i
    
    return z

print(get_Z_Func('aabxaabxcaabxaabxay'))