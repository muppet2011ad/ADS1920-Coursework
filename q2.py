# q2.py written by James Townsend, December 2019
# Tested using Python 3.7.4

factMemo = {0:1,1:1} # This stores the results of all factorisations so we can quickly access them on-demand
childCache = {} # This caches the results of all children so that we do not have to calculate them again when the same numbers come up
descCache = {1:[1,0]} # This caches the results of all descendants that we calculate, saving time on repeated tests (and when the same sequences comes up)

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

def getDescIter(n, pre = None):
    descs = []
    if not pre:
        pre = []
    cGen = getChild(n)
    while cGen not in descs and cGen not in pre:
        descs.append(cGen)
        cGen = getChild(cGen)
    return len(descs)

def getDescendants(n, seq=None):
    if seq == None:
        seq = []
    seq.append(n)
    #print(n)
    if n not in seq[:1] and n == getChild(n):
        return 0
    if seq.count(n) > 1:
        for i in range(seq.index(n),len(seq)):
            descCache[seq[i]] = [getDescIter(seq[i]),1]
            #print("Iteration time motherhecker", seq[i], ":", descCache[seq[i]][0])
        return -1
    if n in descCache:
        #print("getting cache for", n, ":", descCache[n])
        cache = descCache[n]
        if cache[1] == 1:
            return cache[0]-1
        return cache[0]
    res = 1 + getDescendants(getChild(n), seq)
    if n not in descCache:
        #print("Updating cache for", n, ":", res)
        descCache[n] = [res,0]
    return res

def descendants(n1,n2,k): # Returns the number of integers [n1,n2) that have k descendants
    total = 0 # Keeps a total of the number of ints with k descendants
    for i in range(n1,n2):
        getDescendants(i)
        descs = descCache[i][0]
        #print(i, descs)
        if descs == k:
            total += 1
    #print(total)
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
    #print(getDescendants(2))
    #getDescendants(4)
    #getDescendants(10)
    q2test()