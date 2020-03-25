import re
def hail_caesar(enc_str):
    alp = [
      ['A', 'N'],
      ['B', 'O'],
      ['C', 'P'],
      ['D', 'Q'],
      ['E', 'R'],
      ['F', 'S'],
      ['G', 'T'],
      ['H', 'U'],
      ['I', 'V'],
      ['J', 'W'],
      ['K', 'X'],
      ['L', 'Y'],
      ['M', 'Z'],
      ['N', 'A'],
      ['O', 'B'],
      ['P', 'C'],
      ['Q', 'D'],
      ['R', 'E'],
      ['S', 'F'],
      ['T', 'G'],
      ['U', 'H'],
      ['V', 'I'],
      ['W', 'J'],
      ['X', 'K'],
      ['Y', 'L'],
      ['Z', 'M']
    ]
    
    result = ""
    for x in range(0, len(enc_str)):
        if re.match('[0-9+-=%"`:!,|{}^@()#$.<>*?/_&;]', enc_str[x]) or enc_str[x] == ' ' or enc_str[x] == '[' or enc_str[x] == ']':
            result += enc_str[x]
        for y in range(0, len(alp)):
            if alp[y][0] == enc_str[x]:
                result += alp[y][1]
                
    return result