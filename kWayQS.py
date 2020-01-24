import sys

def read_input(filename):
    A = []
    
    try:
        myfile = open(filename, 'r')
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
    for line in myfile:
        A = A + [int(line.strip())]
    myfile.close()
    return A
    
def insertionsort(A): # Insertion sort function
    x = 1
    while x < len(A):
        y = x
        while y > 0 and A[y-1] > A[y]:
            tmp = A[y]
            A[y] = A[y-1]
            A[y-1] = tmp
            y -= 1
        x += 1
    return A
   
def partition(A, k):
    pivots = insertionsort(A[:k]) # Select the first k elements to be our pivots (randomised quicksort) and sorts them (to make comparison easier)
    nonpivots = A[k:] # The elements to slot between the pivots is everything afterwards
    partDict = {} # We keep a dictionary for each part of the list
    for pivot in pivots:
        partDict[pivot] = [] # For every pivot, give it a list in the dictionary. We use this to store all values less than this pivot (but greater than the previous one)
    partDict["end"] = [] # We also need to have a group that stores numbers bigger than the largest pivot
    for integer in nonpivots: # For every integer that isn't a pivot
        done = False # Keep a variable to track whether we've found a place for it
        for pivot in pivots: # Iterate through the pivots
            if integer < pivot: # If the integer is less than the pivot
                partDict[pivot].append(integer) # Store it in the corresponding list
                done = True
                break # Get out of the loop
        if not done: # If we go through all pivots without finding a place
            partDict["end"].append(integer) # We know it has to go in the end list
    partitions = [] # Create a list to store the partitions of the list
    for pivot in pivots: # For every pivot
        partitions.append(partDict[pivot] + [pivot]) # Append the list of the elements smaller than it (and itself) to the partitions
    partitions.append(partDict["end"]) # Add in the final segment
    return partitions # Return this partitions

def quicksort(A, k): # kQS method
    if len(A) <= 2*k: # If the length of the array is too small
        return insertionsort(A) # Sort it by insertion
    partitions = partition(A,k) # Otherwise partition the array
    final = [] # Create a list for the final combination of sorted partitions
    for part in partitions: # For every partition
        final += quicksort(part,k) # Quicksort it and append this to our final list
    return final # Return the result

def main():
    k = int(sys.argv[1])
    filename = sys.argv[2]
    A = read_input(filename)
    print(quicksort(A,k))
    
if __name__ == "__main__":
    main()
