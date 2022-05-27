def compareTriplets(a, b):
    # Write your code here
    res = [0, 0]
    for i in range(3):
        if a[i] > b[i]: res[0] += 1
        elif b[i] > a[i]: res[1] += 1
    return res

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    m = n
    for i in range(1,n+1):
        print(' ' * (m-1) + '#' * i)
        m-=1

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sumAll = sum(arr)
    minimum = sumAll - arr[0]
    maximum = sumAll - arr[0]
    for i in range(1, 5):
        curr = sumAll - arr[i]
        if curr > maximum:
            maximum = curr
        if curr < minimum:
            minimum = curr
    print(str(minimum) + ' ' + str(maximum))