def sort_array(source_array):

    # if array is empty.
    if not source_array:
        return []
    
    # sort the odd ones only.
    odd_sortion = sorted([num for num in source_array if num%2])
    
    i = 0
    for x in range(0, len(source_array)):
        # add sorted odd's to the main array which also contains the even numbers.
        if source_array[x] % 2:
            source_array[x] = odd_sortion[i]
            i = i + 1
    return source_array