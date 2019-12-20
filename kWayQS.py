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
            A[y-1] = A[y]
            y -= 1
        x += 1
    return A
   
    
def partition(A, k):
    # your code goes here
    return ? # whatever you want it to return
    

def quicksort(A, k):
    # your code goes here
    return ? # return value must be argument list A in sorted
    

def main():
    k = int(sys.argv[1])
    filename = sys.argv[2]
    A = read_input(filename)
    print(quicksort(A,k))
    
if __name__ == "__main__":
    main()