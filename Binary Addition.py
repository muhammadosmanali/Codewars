def add_binary(a,b):
    sum = a + b
    if sum == 1:
        binary = format(sum, "01b")
    elif sum == 3 or sum == 2:
        binary = format(sum, "02b")
    elif 4 <= sum <= 7:
        binary = format(sum, "03b")
    elif 8 <= sum <= 15:
        binary = format(sum, "04b")
    elif 16 <= sum <= 31:
        binary = format(sum, "05b")
    elif 32 <= sum <= 63:
        binary = format(sum, "06b")
    elif 64 <= sum <= 127:
        binary = format(sum, "07b")
    elif 128 <= sum <= 255:
        binary = format(sum, "08b")
    elif 256 <= sum <= 510:
        binary = format(sum, "09b")
    elif 511 <= sum <= 1022:
        binary = format(sum, "10b")
    elif 1023 <= sum <= 2046:
        binary = format(sum, "11b")
    elif 2047 <= sum <= 4095:
        binary = format(sum, "12b")
    elif 4096 <= sum <= 8190:
        binary = format(sum, "13b")
    elif 8191 <= sum <= 16382:
        binary = format(sum, "14b")
    elif 16383 <= sum <= 32766:
        binary = format(sum, "15b")
    else:
        binary = format(sum, "16b")
    return binary