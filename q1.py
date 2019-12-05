def hash_quartic(keys):
    table = ["-"]*23
    
    for key in keys:
        hash = (4*key + 7) % 23
        j = 0
        while table[(hash+j**4) % 23] != "-":
            j += 1
        table[(hash+j**4) % 23] = key

    return table

def hash_double(keys):
    table = ["-"]*23

    for key in keys:
        hash = (4*key + 7) % 23
        if table[hash] == "-":
            table[hash] = key
        else:
            offset = 17 - (key % 17)
            while table[(hash + offset) % 23] != "-":
                offset += 17 - (key % 17)
            table[(hash + offset) % 23] = key

    return table