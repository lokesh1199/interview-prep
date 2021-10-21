# Find the ""Kth"" max and min element of an array

def kMax(a: list, k: int):
    b = a[:]
    for i in range(k):
        max = i
        for j in range(i+1, len(b)):
            max = j if b[max] < b[j] else max
        b[i], b[max] = b[max], b[i]
    return b[k-1]


def min(a: list):
    min = a[0]
    for i in a[1:]:
        min = min if min <= i else i
    return min


a = input('list: ').split()
a = [int(i) for i in a]
k = int(input('k: '))

print(f'{k} max: {kMax(a, k)}')
print(f'min: {min(a)}')
