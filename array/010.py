# Given an array of integers where each element represents the max number of
# steps that can be made forward from that element. Write a function to return
# the minimum number of jumps to reach the end of the array (starting from the
# first element). If an element is 0, they cannot move through that element.
# If the end isn’t reachable, return -1.

def findMinJumps(arr):
    if len(arr) < 2:
        return 0
    minJumps = 1

    index = 0
    while index < len(arr):
        currentSteps = arr[index]

        if index + currentSteps >= len(arr) - 1:
            return minJumps
        elif currentSteps == 0:
            return -1

        maxSteps = 1
        for i in range(1, currentSteps):
            if maxSteps < arr[index + i]:
                maxSteps = arr[index + i]

        index += maxSteps
        minJumps += 1

    if index >= len(arr) - 1:
        return minJumps

    return -1


def main():
    arr = list(map(int, input().split()))
    print(findMinJumps(arr))


if __name__ == '__main__':
    main()
