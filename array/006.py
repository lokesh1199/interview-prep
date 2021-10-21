# Find the Union and Intersection of the two sorted arrays

def intersection(a: list, b: list):
    res = []
    for i in a:
        if i in b and i not in res:
            res.append(i)
    return res


def union(a: list, b: list):
    res = a[:]
    for i in b:
        if i not in res:
            res.append(i)
    return res


a = input('list1: ').split()
a = [int(i) for i in a]

b = input('list2: ').split()
b = [int(i) for i in b]

print('union:', union(a, b))
print('intersection:', intersection(a, b))
