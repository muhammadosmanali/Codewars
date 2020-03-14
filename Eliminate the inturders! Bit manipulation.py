def eliminate_set_bits(number):
    new_number = ''
    for x in number:
        if x == '1':
            new_number += x
    
    result = 0
    for x in range(0, len(new_number)):
        if new_number[len(new_number) - 1 - x] == '1':
            result += (2 ** x)
    return result
