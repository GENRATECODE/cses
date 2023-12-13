from itertools import permutations
r=list(set(permutations(input())))
print(len(r))
for i in sorted(r):
    print(''.join(i))

