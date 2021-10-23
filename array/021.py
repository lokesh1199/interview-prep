# Find if there is any subarray with sum equal to 0

def zeroSubArray(a: list):
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            if sum(a[i:j]) == 0:
                return True
    return False


a = [1, -1, 2, -2, 5, -4, -3]
print(zeroSubArray(a))
