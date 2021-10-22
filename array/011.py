# find duplicate in an array of N+1 Integers


def findDuplicate1(a: list):
    found = {}
    for i in a:
        if not found.get(i, None):
            found[i] = 1
        else:
            return i


def findDuplicate2(a: list):
    n = len(a)
    sumOfN = n * (n-1) / 2
    sumOfList = sum(a)
    return sumOfList - int(sumOfN)


a = [1, 3, 4, 5, 2, 5]
print(findDuplicate1(a))
print(findDuplicate2(a))
