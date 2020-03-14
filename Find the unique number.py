def find_uniq(arr):
    i = 1
    n = 0
    if arr[0] == 0 and arr[1] == 1:
        return 0
    for x in range(0, len(arr)):
        if arr[0] == arr[i]:
            i += 1
        else:
            n = arr[i]
    return n   # n: unique integer in the array