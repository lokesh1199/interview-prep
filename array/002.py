# Find the maximum and minimum element in an array

l = input('>> ').split()

min = max = l[0]

for i in l[1:]:
    if min > i:
        min = i
    if max < i:
        max = i

print(min, max)
