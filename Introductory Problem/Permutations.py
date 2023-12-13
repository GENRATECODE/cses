"""
Time limit: 1.00 s Memory limit: 512 MB
A permutation of integers 1,2,…,n
 is called beautiful if there are no adjacent elements whose difference is 1
.

Given n
, construct a beautiful permutation if such a permutation exists.

Input

The only input line contains an integer n
.

Output

Print a beautiful permutation of integers 1,2,…,n
. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".

Constraints
1≤n≤106

Example 1

Input:
5

Output:
4 2 5 3 1

Example 2

Input:
3

Output:
NO SOLUTION
"""
def Permutations(n:int):
    if n==2 or n==3:
        print('NO SOLUTION')
    else:
        for i in range(1,n+1):
            value=2*i
            if value<=n:
                print(value,end=' ')
        for j in range(1,n+1):
            value=2*j-1
            if value<=n:
                print(value,end=' ')
        

n=int(input())
Permutations(n)