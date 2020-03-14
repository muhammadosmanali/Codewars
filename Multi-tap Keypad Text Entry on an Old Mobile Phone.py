def presses(phrase):
    alpArr = [['Aa', 1],
          ['Bb', 2],
          ['Cc', 3],
          ['Dd', 1],
          ['Ee', 2],
          ['Ff', 3],
          ['Gg', 1],
          ['Hh', 2],
          ['Ii', 3],
          ['Jj', 1],
          ['Kk', 2],
          ['Ll', 3],
          ['Mm', 1],
          ['Nn', 2],
          ['Oo', 3],
          ['Pp', 1],
          ['Qq', 2],
          ['Rr', 3],
          ['Ss', 4],
          ['Tt', 1],
          ['Uu', 2],
          ['Vv', 3],
          ['Ww', 1],
          ['Xx', 2],
          ['Yy', 3],
          ['Zz', 4],
        ]
    numbers = [
        ['0', 2],
        ['1', 1],
        ['2', 4],
        ['3', 4],
        ['4', 4],
        ['5', 4],
        ['6', 4],
        ['7', 5],
        ['8', 4],
        ['9', 5],
        ['*', 1],
        ['#', 1]
    ]
    arrLen = len(alpArr)
    numLen = len(numbers)
    result = 0
    for x in phrase:
        if x == ' ':
            result += 1
        for y in range(0, arrLen):
            if x == alpArr[y][0][0] or x == alpArr[y][0][1]:
                result += alpArr[y][1]
    for x in phrase:
        for y in range(0, numLen):
            if x == numbers[y][0]:
                result += numbers[y][1]
    return result