import re
def xo(s):
    s_arr = [char for char in s]
    x_arr = []
    o_arr = []
    for x in s_arr:
        if re.match('[xX]', x):
            x_arr.append(x)
        if re.match('[oO]', x):
            o_arr.append(x)
    
    if x_arr == [] or o_arr == []:
        return True
    
    if len(x_arr) == len(o_arr) and len(x_arr) > 0 and len(o_arr) > 0:
        return True
    
    return False