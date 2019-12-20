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
    if len(A) < 2*k:
        return insertionsort(A)
    partitions = partition(A,k)
    final = []
    for part in partitions:
        final += quicksort(part,k)
    return final

#def testland():
#    print(quicksort([7,6,5,4,3,2,1],3))
#    print(quicksort([7,6,5,4,3,2,1],2))
#    print(quicksort([7,6,5,4,3,2,1],8))
#    print(quicksort([1,4,8,5,2,6,7],3))
#    print(quicksort([2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 16, 17, 18, 20, 21, 22, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39, 40, 41, 42, 46, 48, 49, 50, 51, 52, 53, 54, 55, 58, 59, 60, 61, 65, 66, 67, 68, 71, 73, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 97, 98, 101, 102, 103, 104, 106, 107, 108, 109, 110, 111, 113, 114, 116, 118, 121, 123, 124, 127, 129, 130, 131, 132, 133, 134, 135, 139, 140, 141, 142, 143, 144, 146, 147, 148, 149, 152, 153, 154, 157, 158, 160, 161, 162, 164, 168, 170, 171, 172, 174, 175, 176, 182, 183, 186, 187, 188, 189, 190, 191, 192, 193, 196, 197, 198, 200, 201, 202, 204, 206, 207, 208, 210, 211, 213, 214, 215, 217, 221, 223, 224, 225, 227, 230, 231, 233, 234, 235, 236, 237, 238, 240, 241, 243, 244, 248, 251, 252, 253, 254, 256, 258, 260, 261, 262, 263, 264, 266, 267, 268, 269, 271, 273, 275, 276, 277, 278, 281, 282, 283, 284, 285, 287, 288, 290, 292, 293, 294, 297, 299, 300], 50))

def main():
    #testland()
    k = int(sys.argv[1])
    filename = sys.argv[2]
    A = read_input(filename)
    print(quicksort(A,k))
    
if __name__ == "__main__":
    main()
