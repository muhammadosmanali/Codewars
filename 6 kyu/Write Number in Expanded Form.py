def expanded_form(num):
    #convert int to string
    string = str(num)
    # Reverse the string 
    string = string[::-1]
    result = ''
    arr = []
    for x in range(0, len(string)):
        # x should be greater than zero 
        if int(string[x]) > 0:
            # if greater than zero than add zero to that number in amount of index
            result = string[x] + ('0' * x)
            #Add it to the Array
            arr.append(result)
        
    newstr = ""
    # Again reverse to move it back from reverse to original order
    arr = arr[::-1]
    
    for y in arr:
        newstr = newstr + y + " + "
        
    newstr = newstr[:-3]
    return newstr