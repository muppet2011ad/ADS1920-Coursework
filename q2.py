# q2.py written by James Townsend, December 2019
# Tested using Python 3.7.4

factMemo = {0:1,1:1} # This stores the results of all factorisations so we can quickly access them on-demand
childCache = {} # This caches the results of all children so that we do not have to calculate them again when the same numbers come up
descCache = {1:1} # This caches the results of all descendants that we calculate, saving time on repeated tests (and when the same sequences comes up)

def fact(n): # Recursive function for factorising
    if n in factMemo: # If we have the factorial memoised
        return factMemo[n] # Then just return that
    result = n * fact(n-1) # Otherwise calculate n * the factorial of n-1
    factMemo[n] = result # Memoise that result
    return result # And return it

def getChild(num): # Function to get the child of a number
    if num in childCache: # If we have already worked out the child of a number
        return childCache[num] # Return what we have cached
    total = 0 # Set the total of our sum to be zero
    for digit in str(num): # To iterate over the digits of a number we need to convert it to a string and iterate over the chars
        total += fact(int(digit)) # Add the factorial of our result to the total
    childCache[num] = total # Cache the final result
    return total # Return the final result

def getDescIter(n):
    descs = []
    cGen = getChild(n)
    while cGen not in descs:
        descs.append(cGen)
        cGen = getChild(cGen)
    return len(descs)

def getDescendants(n, seq=[]):
    print(n)
    if n in seq:
        finstance = seq.index(n)
        length = len(seq) - finstance
        descCache[n] = length
        return -1
    if n in descCache:
        print("getting cache for", n, ":", descCache[n])
        return descCache[n]
    res = 1 + getDescendants(getChild(n), seq + [n])
    if n not in descCache:
        descCache[n] = res
    return res

def descendants(n1,n2,k): # Returns the number of integers [n1,n2) that have k descendants
    total = 0 # Keeps a total of the number of ints with k descendants
    for i in range(n1,n2):
        descs = getDescendants(i)
        print(i, descs)
        if descs == k:
            total += 1
    print(total)
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