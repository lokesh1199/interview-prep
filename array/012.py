# Given two sorted arrays arr1[] of size N and arr2[] of size M. Each array is
# sorted in non-decreasing order. Merge the two arrays into one sorted array
# in non-decreasing order without using any extra space.

def merge(a: list, b: list):
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] >= b[j]:
            print(b[j], end=' ')
            j += 1
        else:
            print(a[i], end=' ')
            i += 1

    while i < len(a):
        print(a[i], end=' ')
        i += 1

    while j < len(b):
        print(b[j], end=' ')
        j += 1
    print()


a = [1, 2, 4, 6, 10, 11]
b = [3, 5, 7]
merge(a, b)
