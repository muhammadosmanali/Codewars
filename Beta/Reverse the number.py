def reverse(n):
    n = str(n)
    new_n = ''
    for x in range(0, len(n)):
        new_n += (n[len(n)-1-x])
    result = int(new_n)
    return result