def solution(s):
    newstr = ''
    for char in s:
        if char.islower():
            newstr += char
        elif char.isupper():
            newstr += ' '
            newstr += char
    return newstr