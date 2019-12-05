# q2.py written by James Townsend, December 2019
# Tested using Python 3.7.4

factMemo = {1:1}

def fact(n):
    if n in factMemo:
        return factMemo[n]
    result = n * fact(n-1)
    factMemo[n] = result
    return result

def getChild(num):
    total = 0
    for digit in str(num):
        total += fact(int(digit))
    return total