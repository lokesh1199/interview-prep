# Write a program to cyclically rotate an array by one

def cycleList2(a: list, n: int):
    res = []
    for i in range(len(a)):
        j = (i-n) % len(a)
        res.append(a[j])
    return res


def cycleList1(a: list, n: int):
    return a[-n:] + a[:-n]


a = input('list1: ').split()
n = int(input('n: '))
print(cycleList1(a, n))
print(cycleList2(a, n))
