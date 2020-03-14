def digital_root(n):
    n = str(n)
    i = 0
    length = len(n)
    result = 0
    
    while i < length:
        result += int(n[i])
        
        if i == length-1:
            m = str(result)
            if len(m)>1:
                i = -1
                n = str(result)
                length = len(n)
                result = 0
        i+=1
    return result