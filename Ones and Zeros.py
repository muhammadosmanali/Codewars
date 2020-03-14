def binary_array_to_number(arr):
    count = 0
    for x in arr:
        count = count + 1
        
    new_count = count - 1
    sum = 0
    if count >= 1:
        if arr[new_count] == 1:
            sum = sum + 1
    if count >= 2:
        if arr[new_count - 1] == 1:
            sum = sum + 2
    if count >= 3:
        if arr[new_count - 2] == 1:
            sum = sum + 4
    if count >= 4:
        if arr[new_count - 3] == 1:
            sum = sum + 8
    if count >= 5:
        if arr[new_count - 4] == 1:
            sum = sum + 16
    if count >= 6:
        if arr[new_count - 5] == 1:
            sum = sum + 32
    if count >= 7:
        if arr[new_count - 6] == 1:
            sum = sum + 64
    if count >= 8:
        if arr[new_count - 7] == 1:
            sum = sum + 128
    if count >= 9:
        if arr[new_count - 8] == 1:
            sum = sum + 256
    if count >= 10:
        if arr[new_count - 9] == 1:
            sum = sum + 512
    
        
    return sum