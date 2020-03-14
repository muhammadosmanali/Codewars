def data_reverse(data):
    arr1 = [] 
    arr2 = []
    start = 0
    end = 8
    for x in range(0, int(len(data)/8)):
        while start < end:
            arr1.append(data[start])
            start+=1
        
        arr2 += [arr1]
        arr1 = []
        start = end
        end += 8
    
    arr3 = []
    for x in range(0, len(arr2)):
        arr3.append(arr2[len(arr2)-1-x])
    
    result = []
    for x in arr3:
        result += x
    
    return result