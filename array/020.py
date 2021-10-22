# Given an array of positive and negative numbers, arrange them in an alternate
#  fashion such that every positive number is followed by negative and vice-versa
# maintaining the order of appearance.
# Number of positive and negative numbers need not be equal. If there are more
# positive numbers they appear at the end of the array. If there are more
# negative numbers, they too appear in the end of the array.

def pairPosAndNeg(a: list):
    res = []
    p = n = 0
    flag = 1
    while p < len(a) and n < len(a):
        if a[n] < 0:
            if flag:
                res.append(a[n])
                n += 1
                flag = not flag
        else:
            n += 1
        if a[p] >= 0:
            if not flag:
                res.append(a[p])
                p += 1
                flag = not flag
        else:
            p += 1

    while p < len(a):
        if a[p] >= 0:
            res.append(a[p])
        p += 1

    while n < len(a):
        if a[n] < 0:
            res.append(a[n])
        n += 1

    return res


a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

print(pairPosAndNeg(a))
