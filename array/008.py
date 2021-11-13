# find Largest sum contiguous Subarray

def maxContigousSum(a: list):
    if not len(a):
        return 0
    maxSum = a[0]
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            curSum = sum(a[i:j])
            maxSum = curSum if maxSum < curSum else maxSum
    return maxSum


a = list(map(int, input().split()))
print(maxContigousSum(a))
