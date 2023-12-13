"""A Gray code is a list of all 2n
 bit strings of length n
, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).

Your task is to create a Gray code for a given length n
.

Input

The only input line has an integer n
.

Output

Print 2n
 lines that describe the Gray code. You can print any valid solution.

Constraints
1≤n≤16

Example

Input:
2

Output:
00
01
11
10"""
#binary
def binary(n,lens):
    a='1'
    b='0'
    check=n
    result=list()
    result1=''
    if n==0:
        result.append(b*lens)
    while n!=0:
        if n%2==0:
            result.append(b)
        else:
            result.append(a)
        n=n//2
    
    if len(result)!=lens and check!=0:
        dummy=lens-len(result)
        result.append(b*dummy)

    result.reverse()
    return result1.join(result)

#gray code
def gray_code(n:int,lens:int):
    b=binary(n,lens)
    gray=''
    start=1 
    for i in b:
        if start==1:
            gray+=i
            prev=i
            start-=1
        elif prev=='0' and i=='0':
            gray+='0'
            prev=i
        elif prev=='0' and i=='1':
            gray+='1'
            prev=i
        elif prev=='1' and i=='1':
            gray+='0'
            prev=i
        elif prev=='1' and i=='0':
            gray+='1'
            prev=i
    return gray

#print
def print_g(n:int)->int:
    for i in range(2**n):
        print(gray_code(i,n))


print_g(int(input()))