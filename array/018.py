# find all pairs on integer array whose sum is equal to given number

def getPairs(a: list, s: int):
    res = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == s:
                res.append((a[i], a[j]))
    return res


a = [1, 5, 7, -1, 5]
s = 6
print(getPairs(a, s))
