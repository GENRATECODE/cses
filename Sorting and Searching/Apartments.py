"""Time limit: 1.00 s Memory limit: 512 MB
There are n
 applicants and m
 free apartments. Your task is to distribute the apartments so that as many applicants as possible will get an apartment.

Each applicant has a desired apartment size, and they will accept any apartment whose size is close enough to the desired size.

Input

The first input line has three integers n
, m
, and k
: the number of applicants, the number of apartments, and the maximum allowed difference.

The next line contains n
 integers a1,a2,…,an
: the desired apartment size of each applicant. If the desired size of an applicant is x
, he or she will accept any apartment whose size is between x−k
 and x+k
.

The last line contains m
 integers b1,b2,…,bm
: the size of each apartment.

Output

Print one integer: the number of applicants who will get an apartment.

Constraints
1≤n,m≤2⋅105

0≤k≤109

1≤ai,bi≤109

Example

Input:
4 3 5
60 45 80 60
30 60 75

Output:
2"""
# map(int,input().split())
n,m,k=map(int,input().split())
client=list(map(int,input().split()))
apartments=list(map(int,input().split()))
client.sort()
apartments.sort()
acquired_apartments=0
# count for acquiring appointments in range [x-k , x + k] with
i,j,c=0,0,0
while i<n and j<m:
    if client[i]+k<apartments[j]:
        i+=1
    elif client[i]-k>apartments[j]:
        j+=1
    else:
        i+=1
        j+=1
        c+=1
print(c)