# find common elements In 3 sorted arrays


def findCommon(a: list, b: list, c: list):
    res = []
    i = j = k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] < b[j] or a[i] < c[k]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        elif a[i] > c[k]:
            k += 1
        else:
            res.append(a[i])
            i += 1
            j += 1
            k += 1
    return res


a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]

print(findCommon(a, b, c))
