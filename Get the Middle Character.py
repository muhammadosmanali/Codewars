def get_middle(s):
    count = 0
    for x in s:
        count = count + 1
    if count == 1:
        return s
    elif count == 2:
        return s
    elif count % 2 == 0:
        middle = count / 2
        text = s[middle-1] + s[middle]
        return text
    else:
        middle = count / 2
        text = s[middle]
        return text