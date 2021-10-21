# Reverse the array

list1 = input('>> ').split()
n = len(list1)

for i in range(n//2):
    list1[i], list1[n-i-1] = list1[n-i-1], list1[i]

print(list1)
