import math


def diagonalDifference(arr):
    step = int(math.sqrt(len(arr)))
    firstLine = 0
    rightRead = 0
    leftRead = step - 1
    sumRight = 0
    sumLeft = 0
    for x in range(0, step):
        sumRight += abs(arr[firstLine + rightRead])
        print(f"right {abs(arr[firstLine + rightRead])}")
        sumLeft += abs(arr[firstLine + leftRead])
        print(f"left {arr[firstLine + leftRead]}")
        rightRead += 1
        leftRead -= 1
        firstLine += step
    return abs(sumRight - sumLeft)
    # print(sumLeft)
