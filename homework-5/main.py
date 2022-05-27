# Maria plays college basketball and wants to go pro. 
# Each season she maintains a record of her play. She tabulates the number of times 
# she breaks her season record for most points and least points in a game. 
# Points scored in the first game establish her record for the season, and she begins counting from there.
# Given the scores for a season, determine the number of times Maria breaks 
# her records for most and least points scored during the season.

# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    maxCounter = 0
    minCounter = 0
    maximum = scores[0]
    minimum = scores[0]
    for el in scores:
        if el > maximum:
            maximum = el
            maxCounter += 1
        if el < minimum:
            minimum = el
            minCounter += 1
    return [maxCounter, minCounter]

# https://www.hackerrank.com/challenges/kangaroo/problem

# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
# 

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 == v2: return 'NO'
    if x1 == x2: return 'YES'

    if x1 > x2 and v2 > v1 and (x1-x2) % (v2-v1) == 0:
        return 'YES'
    elif x2 > x1 and v1 > v2 and (x2-x1) % (v1-v2) == 0:
        return 'YES'
    else: return 'NO'