# find Largest sum contiguous Subarray

def maxContigousSum(a: list):
    if not len(a):
        return
    maxSum = a[0]
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            print(a[i:j])
            curSum = sum(a[i:j])
            maxSum = curSum if maxSum < curSum else maxSum
    return maxSum


a = input('list1: ').split()
a = [int(i) for i in a]
print(maxContigousSum(a))
