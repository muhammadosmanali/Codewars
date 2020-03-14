import math

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if is_square(sq):
        present = math.sqrt(sq)
        next1 = present + 1
        next2 = next1 * next1
        return next2 
    else:
        return -1