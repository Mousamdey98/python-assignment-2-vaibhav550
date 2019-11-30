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
