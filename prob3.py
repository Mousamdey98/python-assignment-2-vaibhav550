def nondec(L):
    count = 0
    for i in range(0, len(L) - 1):

        if (L[i] > L[i + 1]):
            count += 1
            temp = i

    if (count == 1):
        if (L[len(L) - 1] == L[temp + 1] or temp == 0):
            print('True')
        elif (L[temp - 1] - L[temp + 1] <= 0):
            print("True")
        elif (L[temp] - L[temp + 2] > 0):
            print('False')
        else:
            print("True")
    elif (count == 0):
        print('True')

    else:
        print("False")


li = list(map(int, input().split()))

nondec(li)


