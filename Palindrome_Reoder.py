"""Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).

Input

The only input line has a string of length n
 consisting of characters A–Z.

Output

Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".

Constraints
1≤n≤106

Example

Input:
AAAACACBA

Output:
AACABACAA"""

from collections import defaultdict
def Palindrome_Reoder(strings:str):
    temp=defaultdict(int)
    s=set()
    for i in strings:
        temp[i]+=1
        s.add(i)
    s=list(sorted(''.join(list(s))))
    right=''
    left=''
    count=1
    for i in s :
        while temp[i]!=0: 
            if (temp[i])%2==0:
                temp[i]-=2
                right+=i
                left+=i
            elif count==1 :
                temp[i]-=1
                prev=i
                count-=1
            else: 
                return 'NO SOLUTION'
    if len(strings)%2==1:
        return right+prev+''.join(sorted(left,reverse=True))
    else:
        return right+''.join(sorted(left,reverse=True))
 
# ain
 
if __name__=="__main__":
    strings=input()
    print(Palindrome_Reoder(strings))
