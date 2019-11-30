s = input()
s1 = ""
k = int(input())
lo = list(s.split(" "))
mini = len(lo[0])
for i in range(len(lo)):
    if len(lo[i]) > mini:
        mini = len(lo[i])
if k < mini:
    print("null")
else:
    r = k
    j = 0
    while r <= len(s) + k:
        if r >= len(s) - 1:
            r = len(s) - 1
            break
        while s[r] != " ":
            r -= 1
        s1 += s[j:r] + "\n"
        j = r + 1
        r += k + 1
    s1 += s[j:r + 1]
    print(s1)