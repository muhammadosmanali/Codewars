import numpy as np

def delete_nth(order,max_e):
    new_order = []
    for x in order:
        if x not in new_order:
            new_order.append(x)
    
    new_lst = []
    for y in new_order:
        count = 0
        for z in range(0, len(order)):
            if order[z] == y:
                count += 1
                if count > max_e:
                    new_lst.append(z)
                    
    new_lst.sort()
    result = np.delete(order, new_lst).tolist()
                
    return result