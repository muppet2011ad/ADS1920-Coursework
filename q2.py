# q2.py written by James Townsend, December 2019
# Tested using Python 3.7.4

factMemo = {0:1,1:1}
childCache = {}
descCache = {}

def fact(n):
    if n in factMemo:
        return factMemo[n]
    result = n * fact(n-1)
    factMemo[n] = result
    return result

def getChild(num):
    if num in childCache:
        return childCache[num]
    total = 0
    for digit in str(num):
        total += fact(int(digit))
    childCache[num] = total
    return total

def descendants(n1,n2,k):
    total = 0
    for n in range(n1,n2):
        if n in descCache:
            descs = descCache[n]
        else:
            descs = []
            currentGen = getChild(n)
            while currentGen not in descs:
                descs.append(currentGen)
                if currentGen in descCache and getChild(currentGen) != currentGen:
                    cached = descCache[currentGen]
                    if cached[len(cached)-1] in (n,currentGen):
                        cached = cached[:-1]
                    if not set(descs).intersection(set(cached)):
                        descs = descs + descCache[currentGen]
                        if descs[len(descs)-1] in (n,currentGen):
                            descs = descs[:-1]
                        break
                    else:
                        currentGen = getChild(currentGen)
                else:
                    currentGen = getChild(currentGen)
            descCache[n] = descs
            
        if len(descs) == k:
            total += 1
    return total
            
def q2test():
    assert descendants(1,2,1) == 1
    print("t1 done")
    assert descendants(1,200,1) == 6
    print("t2 done")
    assert descendants(1,200,2) == 2
    print("t3 done")
    assert descendants(1,2000,3) == 33
    print("t4 done")
    assert descendants(4000,6000,3) == 36
    print("t5 done")
    assert descendants(123456,654321,20) == 4015
    print("t6 done")
    assert descendants(1,1000000,59) == 402
    print("t7 done")
    assert descendants(1,1000000,60) == 0
    print("All tests completed")


if __name__ == "__main__":
    q2test()