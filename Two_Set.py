"""
Your task is to divide the numbers 1,2,…,n
 into two sets of equal sum.

Input

The only input line contains an integer n
.

Output

Print "YES", if the division is possible, and "NO" otherwise.

After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.

Constraints
1≤n≤106

Example 1

Input:
7

Output:
YES
4
1 2 4 7
3
3 5 6

Example 2

Input:
6

Output:
NO
"""
def two_set(n:int):
    su=n*(n+1)/2
    a,b=set(),set()
    if su%2==1:
        print("NO")
        return 
    else:
        su=su/2
        print('YES')
        for i in range(n, 0, -1):
            if su >= i:
              su -= i
              a.add(i)
            else:
               b.add(i)
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)



n=int(input())
two_set(n)

