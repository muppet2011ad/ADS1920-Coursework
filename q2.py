# q2.py written by James Townsend, December 2019
# Tested using Python 3.7.4

factMemo = {0:1,1:1} # This stores the results of all factorisations so we can quickly access them on-demand
childCache = {} # This caches the results of all children so that we do not have to calculate them again when the same numbers come up
descCache = {} # This caches the results of all descendants that we calculate, saving time on repeated tests (and when the same sequences comes up)

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

def descendants(n1,n2,k): # Returns the number of integers [n1,n2) that have k descendants
    total = 0 # Keeps a total of the number of ints with k descendants
    for n in range(n1,n2): # Iterate through the range
        if n in descCache: # If we have already calculated the descendants for this number (perhaps from a previous test)
            descs = descCache[n] # Get our descendants from the cache
        else: # Otherwise
            descs = [] # Start with an empty list for descendants
            currentGen = getChild(n) # We will solve this by iterating through the generations - this gets the first child
            while currentGen not in descs: # Whilst we're looking at a number that we haven't seen yet
                descs.append(currentGen) # Append it to our list of descendants
                if currentGen in descCache and getChild(currentGen) != currentGen: # If the number we're looking at has been cached and the number isn't its own child
                    cached = descCache[currentGen] # Get the cached descendants
                    if cached[len(cached)-1] in (n,currentGen): # Sometimes the last element of the cached sequence is the number we started with
                        cached = cached[:-1] # If so, just leave it out
                    if not set(descs).intersection(set(cached)): # Convert both our descendants and the cache to sets so we can find their intersection - if there are no common elements then we can use the cache
                        descs = descs + descCache[currentGen] # Append the cache
                        if descs[len(descs)-1] in (n,currentGen): # Do we need this?
                            descs = descs[:-1]
                        break # If we've appended a cached list of descendants, then we don't need to iterate anymore
                    else:
                        currentGen = getChild(currentGen) # If we can't use the cache, find the next child
                else:
                    currentGen = getChild(currentGen) # If we can't use the cache, find the next child
            descCache[n] = descs # Update the cache with the list of descendants we found
            
        if len(descs) == k: # If the length of the descendants list is k
            total += 1 # Increment our counter
    return total # Return the total at the end
            
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