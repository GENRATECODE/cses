"""You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n
 characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1≤n≤106

Example

Input:
ATTCGGGA

Output:
3
"""
from collections import defaultdict
def Repetitions(string:list)->int:
    cur=''
    max_c=0
    count=0
    for i in string:
        if i ==cur:
            count+=1
        else:
            max_c=max(max_c,count)
            count=1
            cur=i
    return max(max_c,count)
strings=list(input())
print(Repetitions(strings))
