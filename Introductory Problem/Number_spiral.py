"""
A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:

Your task is to find out the number in row y
 and column x
.

Input

The first input line contains an integer t
: the number of tests.

After this, there are t
 lines, each containing integers y
 and x
.

Output

For each test, print the number in row y
 and column x
.

Constraints
1≤t≤105

1≤y,x≤109

Example

Input:
3
2 3
1 1
4 2

Output:
8
1
15
"""
def spiral(x:int,y:int):
    if x>=y:
        if x%2==0:
            return (x-1)*(x-1)+(x-y)+x
        else:
            return (x-1)*(x-1)+y
    else:
        if y%2==0:
            return (y-1)*(y-1)+x
        else:
            return (y-1)*(y-1)+y+(y-x)



for i in range(int(input())):
    y,x=map(int,input().split())
    print(spiral(y,x))