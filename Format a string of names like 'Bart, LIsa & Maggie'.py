def namelist(names):
    length = len(names)
    result = ''
    if length == 1:
        return names[0]['name']
    for x in range(0, length):
        if x < length - 2:
            result += names[x]['name']
            result += ', '
        elif x == length - 2:
            result += names[x]['name']
        elif x == length - 1:
            result += ' & '
            result += names[x]['name']
    return result