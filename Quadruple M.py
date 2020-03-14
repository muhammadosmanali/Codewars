import statistics
def list_mix(ls):
    result = []
    
    result.append(max(ls))
    
    min_num = min(ls)
    if isinstance(min_num, float):
        minimum = float("%.2f" % min_num)
        result.append(minimum)
    else:
        result.append(min_num)
    
    median = statistics.median(ls)
    if isinstance(median, float):
        median = float("%.2f" % median)
    result.append(median)
    
    sum = 0
    for x in ls:
        sum += x
    mean = sum / len(ls)
    if isinstance(mean, float):
        mean = float("%.2f" % mean)
    result.append(mean)
    
    return result