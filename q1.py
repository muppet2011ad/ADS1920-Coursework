# q1.py written by jsbl33, December 2019
# Tested using Python 3.8.1 (because that's what happens to be in the Manjaro repos)
# If buckets cannot be found, the function will output this in the console.

def hash_quartic(keys):
    table = ["-"]*23 # Initialise hash table array
    
    for key in keys: # Iterate over the keys we want to add
        attempts = []
        if "-" not in table: # If there are no empty buckets,
            break # Stop trying to add keys since we can't possible add anymore
        hash = (4*key + 7) % 23 # Calculate the hash of the key
        j = 0 # Start counting j from zero
        success = True
        while table[(hash+j**4) % 23] != "-": # Iterate until we land on an empty bucket
            attempts.append((hash+j**4) % 23)
            if len(attempts) > 1 and attempts[:len(attempts)//2] == attempts[len(attempts)//2:]: # If we're repeating ourself (which happens when we can't find a bucket)
                print("failed to find bucket with quartic probing, skipping key") # Output it
                success = False
                break # Skip the key
            j += 1 # Increment j
        if success:
            table[(hash+j**4) % 23] = key # Once we have our bucket, set the data

    return table # Return the finished hash table

def hash_double(keys):
    table = ["-"]*23 # Initialise hash table array

    for key in keys: # Iterate over the keys we want to add
        attempts = []
        hash = (4*key + 7) % 23 # Calculate the hash of the key
        if table[hash] == "-": # If the location at the hash is empty, then it's easy
            table[hash] = key # We just set the data at that location to be our key
        else: # If it's not easy
            offset = 17 - (key % 17) # Calculate the offset using the secondary hash
            success = True
            while table[(hash + offset) % 23] != "-": # Whilst the location at hash + offset is not free
                if (hash + offset) % 23 in attempts: # If we've already done this bucket then we're not going to get anywhere from here
                    print("failed to find bucket with double hashing, skipping key") # Output that we can't get a bucket
                    success = False # And give up
                    break
                attempts.append((hash + offset) % 23)
                offset += 17 - (key % 17) # Calculate a new offset using the secondary hash
            if success:
                table[(hash + offset) % 23] = key # Once we have an empty bucket, store the key there

    return table # Return the finished hash table