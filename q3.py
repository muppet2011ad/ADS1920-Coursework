# jsbl33 December 2019
# Tested using Python 3.8.1
    
def LP(string):
    longestOdd = LOP(string) # We already have a function for finding the longest odd, we might as well use it

    longestEven = 0 # Keep a variable to track the longest even we've seen

    for i in range(1,len(string)): # Iterate over the different centre points in the string (we have two for each value of i since this is an even palindrome)
        centreL = string[i-1] # Our centre-left pointer is at i-1
        centreR = string[i] # Our centre-right pointer is at i
        if centreL != centreR: # If they don't equal each other
            continue # There's no palindrome in site, so we might as well move on
        ptrL = i - 1
        ptrR = i # Create pointers for the left and right of the string
        while True: # Iterate
            if ptrL - 1 < 0 or ptrR + 1 > len(string) - 1: # If incrementing/decrementing either pointer would go out of range,
                break # Break out of the loop
            ptrL -= 1
            ptrR += 1 # Otherwise we can safely update the pointers
            if string[ptrL] != string[ptrR]: # If the characters at each pointer don't match, 
                break # Break out of the loop
        length = ptrR - ptrL + 1 # Once out of the loop, calculate the length of the palindrome based on pointer values
        if length > longestEven: # If it's the longest one we've seen so far
            longestEven = length # Store it
    
    return max((longestEven,longestOdd)) # Return whichever is longest out of the odd and even palindromes

        
def LP2(string):
    longest = 0 # Keep track of the longest we get
    for i in range(0, len(string)): # Iterate over the possible starting locations for our "loop" around the string
        toTest = string[i:] + string[:i] # Construct a string composed of everything after i followed by everything before it
        longTest = LP(toTest) # Get the longest palindrome in the string from LP
        if longTest > longest: # If it's the longest one we've seen so far,
            longest = longTest # Update the longest variable
    return longest # Return the result