# An University has the following grading policy:
#
# Every student receives a  in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:
#
# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    # grades.pop(0)
    for i in range(0, len(grades)):
        if (grades[i] < 38):
            continue
        if (grades[i]+1) % 5 == 0:
            grades[i]+= 1
        elif (grades[i]+2) % 5 == 0:
            grades[i]+= 2
    return grades

# https://www.hackerrank.com/challenges/apple-and-orange/problem

# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    applesInRange = 0
    orangesInRange = 0
    for apl in apples:
        if (a+apl) >= s and (a+apl) <= t:
            applesInRange+= 1
    for org in oranges:
        if (b+org) >= s and (b+org) <= t:
            orangesInRange+= 1
    print(applesInRange)
    print(orangesInRange)

# You are in charge of the cake for a child's birthday. 
# You have decided the cake will have one candle for each year of their total age. 
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

def birthdayCakeCandles(candles):
    # Write your code here
    tallest = candles[0]
    counter = 1
    for i in range(1, len(candles)):
        if (candles[i] > tallest):
            tallest = candles[i]
            counter = 1
        elif (candles[i] == tallest):
            counter += 1
    return counter