"""
You are given an array of length N intially zeros and you are given q queries 
where each query has (L,R) represents subarray arr[L].....arr[R]
You need to update each element by 1 and print the final array
"""

n = 10
diff_arr = [0]*(n+1)
queries = [[2,6],[3,8],[5,9],[1,4],[2,3]]
for l,r in queries:
    diff_arr[l] += 1
    diff_arr[r+1] -= 1

updated_arr = [0]*n
for i in range(n):
    if i == 0:
        updated_arr[i] = diff_arr[i]
    else:
        updated_arr[i] = diff_arr[i] + updated_arr[i-1]

print(updated_arr)