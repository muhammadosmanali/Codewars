def pig_it(text):
    arr = text.split(' ')
    result = []
    for item in arr:
        if item.isalpha():
            item = item[1:] + item[0] + "ay"
        result.append(item)
    
    str = ' '.join(result)
    return st