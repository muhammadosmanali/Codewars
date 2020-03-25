def divisors(integer):
    result = []
    for x in range(2, integer):
        if integer % x == 0:
            result.append(x)
    
    if result == []:
        return "{} is prime".format(integer)
    return result