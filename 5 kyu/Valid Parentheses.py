def valid_parentheses(string):
    bracket_map = {"[": "]", "{": "}", "(": ")"}
    x = ''.join([i for i in string if i == "(" or i == ")"])
    stack = []
    for b in x:
        if b in bracket_map:
            stack.append(bracket_map[b])
        elif not stack or b != stack.pop():
            return False
    return not stack