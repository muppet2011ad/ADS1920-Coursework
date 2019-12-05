# q1.py written by James Townsend, December 2019
# Tested using Python 3.7.4

def hash_quartic(keys):
    table = ["-"]*23 # Initialise hash table array
    
    for key in keys: # Iterate over the keys we want to add
        hash = (4*key + 7) % 23 # Calculate the hash of the key
        j = 0 # Start counting j from zero
        while table[(hash+j**4) % 23] != "-": # Iterate until we land on an empty bucket
            j += 1 # Increment j
        table[(hash+j**4) % 23] = key # Once we have our bucket, set the data

    return table # Return the finished hash table

def hash_double(keys):
    table = ["-"]*23 # Initialise hash table array

    for key in keys: # Iterate over the keys we want to add
        hash = (4*key + 7) % 23 # Calculate the hash of the key
        if table[hash] == "-": # If the location at the hash is empty, then it's easy
            table[hash] = key # We just set the data at that location to be our key
        else: # If it's not easy
            offset = 17 - (key % 17) # Calculate the offset using the secondary hash
            while table[(hash + offset) % 23] != "-": # Whilst the location at hash + offset is not free
                offset += 17 - (key % 17) # Calculate a new offset using the secondary hash
            table[(hash + offset) % 23] = key # Once we have an empty bucket, store the key there

    return table # Return the finished hash table