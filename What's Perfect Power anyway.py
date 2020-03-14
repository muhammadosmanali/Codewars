def isPP(n):    
    for x in range(2, 20):
        root = n ** (1/float(x))
        if int(root + 0.5) ** x == n:
            return [int(root+0.5),x]
    return None
 