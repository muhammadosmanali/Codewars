def iq_test(numbers):
    even = 0
    odd = 0
    numbers = numbers.split(" ")
    for x in numbers:
        if int(x) % 2 == 0:
            even += 1
        else:
            odd += 1
    str = ""
    i = 1
    if even < odd:
        for y in numbers:
            if int(y) % 2 == 0:
                return i
            i += 1
    else:
        for y in numbers:
            if int(y) % 2 != 0:
                return i
            i += 1