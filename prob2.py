L = list(map(int, input().split(' ')))
k = int(input())
L1 = []
sum = 0

for i in range(0, len(L) - 1):

    if (sum + L[i] <= k):
        sum = sum + L[i]
        L1.append(L[i])



    else:
        break
if (sum == k):
    print(L1)
else:
    print(None)
    
    
'''I think the written below code will iter with best'''
import itertools
L = list(map(int, input().split(' ')))
k = int(input())
sum = 0


for i,j,l in itertools.combinations(L):
    final = []
    if int(i) + int(j) + int(l) == k:
        final.append(i)
        final.append(j)
        final.append(l)
        print(final)
