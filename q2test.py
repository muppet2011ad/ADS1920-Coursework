#q2test.py
#algorithms and data structures assignment 2019-20 q2
#matthew johnson 22 november 2019

#####################################################

import cProfile

fact = [1,1,2,6,24,120,720,5040,40320,362880]
childCache = {} # This caches the results of all children so that we do not have to calculate them again when the same numbers come up
descCache = {1:[1,0]} # This caches the results of all descendants that we calculate, saving time on repeated tests (and when the same sequences comes up)
def getChild(num): # Function to get the child of a number
    if num in childCache: # If we have already worked out the child of a number
        return childCache[num] # Return what we have cached
    total = 0 # Set the total of our sum to be zero
    for digit in str(num): # To iterate over the digits of a number we need to convert it to a string and iterate over the chars
        total += fact[int(digit)] # Add the factorial of our result to the total
    childCache[num] = total # Cache the final result
    return total # Return the final result
def getDescIter(n): # Little iterative algorithm used to find the number of descendents for numbers that occur in a loop (e.g. 169)
    descs = [] # Empty list of descendants
    cGen = getChild(n) # Get the next generation
    while cGen not in descs: # While we haven't seen it before,
        descs.append(cGen) # Append it to our list of descendants
        cGen = getChild(cGen) # Get the next generation
    return len(descs) # Return the number of descendants
def getDescendants(n, seq=None): # Recursive function that returns the number of descendants of any given number
    if not seq: # If a previous sequence has not been specified, 
        seq = [] # Initialise an empty list for it
    seq.append(n) # Append the current value to the sequence list
    if n != seq[0] and n == getChild(n): # If the current value isn't the number whose descendants we're after (i.e. seq[0]) but it is it's own child
        return 0 # We're at the end of the sequence so return 0
    if n in seq[:-1]: # If we've encountered this number before, then we must be in a "loop" of numbers
        for i in range(seq.index(n),len(seq)): # Iterate over all of the numbers in the loop
            descCache[seq[i]] = [getDescIter(seq[i]),1] # For each of them, iteratively find their descendants (trying to do it recursively will end in a loop)
        return -1 # We've gone past the end of the valid sequence of descendants here, so return -1
    if n in descCache: # If we've seen this value before
        cache = descCache[n] # Get the cached value
        if cache[1] == 1: # The cached value has two parts - the number of descendants and a 'danger' flag. The danger flag is 1 if the number is part of a loop and 0 otherwise.
            return cache[0]-1 # If the 'danger' flag is set, then we need to return one less than the cached value
        return cache[0] # Otherwise return 0
    res = 1 + getDescendants(getChild(n), seq) # Recursive call if none of the above conditions are true
    if n not in descCache: # If we haven't dealt with n before,
        descCache[n] = [res,0] # Cache whatever we got as the result
    return res # Return the result (this isn't actually accurate for the original n, but is required for the recursion to work)
def descendants(n1,n2,k): # Returns the number of integers [n1,n2) that have k descendants
    total = 0 # Keeps a total of the number of ints with k descendants
    for i in range(n1,n2): # Iterate over the set of numbers
        getDescendants(i) # Get the descendants of each
        if descCache[i][0] == k: # If the number of descendants matches k
            total += 1 # Increment the total
    return total # Return the total

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

cProfile.run("q2test()")