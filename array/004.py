#  Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
def sort(a: list):
    zeros = ones = twos = 0

    for i in a:
        if i == 0:
            zeros += 1
        elif i == 1:
            ones += 1
        else:
            twos += 1

    return [0] * zeros + [1] * ones + [2] * twos


a = input('list: ').split()
a = [int(i) for i in a]

print(sort(a))
