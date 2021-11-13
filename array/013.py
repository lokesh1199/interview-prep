#  Kadane's Algorithm (maximum sum of contigous subarray)

def maxSum(arr):
    globalMax = previousMax = arr[0] if len(arr) else 0

    for elem in arr[1:]:
        includingPrevious = previousMax + elem
        excludingPrevious = elem

        if globalMax < includingPrevious:
            globalMax = includingPrevious
        elif globalMax < excludingPrevious:
            globalMax = excludingPrevious

        previousMax = includingPrevious

    return globalMax


def main():
    arr = list(map(int, input().split()))
    print(maxSum(arr))


if __name__ == '__main__':
    main()
