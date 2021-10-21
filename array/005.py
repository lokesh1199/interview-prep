# Move all the negative elements to one side of the array

def negativeToOneSide(a: list):
    k = 0
    for i in range(len(a)):
        if a[i] < 0:
            a[i], a[k] = a[k], a[i]
            k += 1


a = input('list: ').split()
a = [int(i) for i in a]
negativeToOneSide(a)
print(a)
