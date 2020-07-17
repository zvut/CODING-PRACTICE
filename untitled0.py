# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:23:48 2020

@author: MrMaak
"""

# STRING COMPRESSION

# Given an array of characters, compress it in-place.

# The length after compression must always be smaller than or equal to the original array.

# Every element of the array should be a character (not int) of length 1.

# After you are done modifying the input array in-place, return the new length of the array.

 
# Follow up:
# Could you solve it using only O(1) extra space?

 
# Example 1:

# Input:
# ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

# Example 2:

# Input:
# ["a"]

# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]

# Explanation:
# Nothing is replaced.
 

# Example 3:

# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.


def compression(arr):
    if arr == None or len(arr) < 1:
        return 0;
    start, end, index = 0,0,0
    while start < len(arr):
        end=start
        while end < len(arr) and arr[start]==arr[end]:
            end+=1
        arr[index]=arr[start]
        index+=1
        if end-start>1:
            for s in str(end-start):
                arr[index]=s
                index+=1
        start=end
    return index
    
arr=["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]
print(compression(arr))




















