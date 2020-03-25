def next_bigger(n):
    exceed = n + 100000
    number = n
    if 0 < n <= 10:
        return -1
    
    arr = []
    number = str(n)
    for x in number:
        arr.append(x)
    arr.sort()
    
    while True:
        n = n + 1
        new_arr = []
        for y in str(n):
            new_arr.append(y)
        new_arr.sort()
        if arr == new_arr:
            break
        if n > exceed:
            return -1
    return n
 