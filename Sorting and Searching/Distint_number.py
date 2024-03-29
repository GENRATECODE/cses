"""
Distinct Numbers
You are given a list of n
 integers, and your task is to calculate the number of distinct values in the list.

Input

The first input line has an integer n
: the number of values.

The second line has n
 integers x1,x2,…,xn
.

Output

Print one integers: the number of distinct values.

Constraints
1≤n≤2⋅105

1≤xi≤109

Example

Input:
5
2 3 2 2 3

Output:
2

"""
def distinct_number(lst):
    temp=0
    count=0
    for i in lst:
        if temp!=i:
            count+=1
        temp=i
    print(count)

if __name__=="__main__":
    values=int(input())
    lst=list(map(int,input().split()))
    lst.sort()

    distinct_number(lst)