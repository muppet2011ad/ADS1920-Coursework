# q2.py written by James Townsend, December 2019
# Tested using Python 3.7.4

factMemo = {0:1,1:1}
descCache = {}

def fact(n):
    if n in factMemo:
        return factMemo[n]
    result = n * fact(n-1)
    factMemo[n] = result
    return result

def getChild(num):
    if num in descCache:
        return descCache[num]
    total = 0
    for digit in str(num):
        total += fact(int(digit))
    descCache[num] = total
    return total

def descendants(n1,n2,k):
    total = 0
    for n in range(n1,n2):
        descendants = []
        currentGen = n
        while currentGen not in descendants:
            descendants.append(currentGen)
            currentGen = getChild(currentGen)
        if len(descendants) > 1:
            descendants = descendants[1:]
        if len(descendants) == k:
            total += 1
    return total
            
def q2test():
    assert descendants(1,2,1) == 1
    assert descendants(1,200,1) == 6
    assert descendants(1,200,2) == 2
    assert descendants(1,2000,3) == 33
    assert descendants(4000,6000,3) == 36
    assert descendants(123456,654321,20) == 4015
    assert descendants(1,1000000,59) == 402
    assert descendants(1,1000000,60) == 0
    print("All tests completed")

q2test()