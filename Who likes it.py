def likes(names):
    count = 0
    for x in names:
        count = count + 1
    if count == 0:
        return "no one likes this"
    if count == 1:
        return names[0] + ' likes this'
    elif count == 2:
        return names[0]+ " and "+ names[1]+ " like this" 
    elif count == 3:
        return names[0]+ ", "+ names[1]+" and "+ names[2]+ " like this" 
    elif count > 3:
        i = count - 2
        return names[0] + ", "+ names[1]+ " and "+ str(i) + " others like this" 