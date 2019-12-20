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


def insertionsort(A):
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
    nonpivots = A[k:]
    partDict = {}
    for pivot in pivots:
        partDict[pivot] = []
    partDict["end"] = []
    for integer in nonpivots:
        done = False
        for pivot in pivots:
            if integer < pivot:
                partDict[pivot].append(integer)
                done = True
                break
        if not done:
            partDict["end"].append(integer)
    partitions = []
    for pivot in pivots:
        partitions.append(partDict[pivot] + [pivot])
    partitions.append(partDict["end"])
    return partitions
    
    

def quicksort(A, k):
    print(partition([1,7,2,6,3,4,5],k))
    

def main():
    #k = int(sys.argv[1])
    #filename = sys.argv[2]
    #A = read_input(filename)
    print(quicksort([],3))
    
if __name__ == "__main__":
    main()