def get_score(n):
    result = 0
    for x in range(1, n+1):
        result = result + (50*x)
    return result