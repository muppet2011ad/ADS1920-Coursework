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
    # your code goes here
    return ? # return value must be argument list A in sorted
   
    
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