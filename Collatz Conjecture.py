def collatz(n):
    steps = 0
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n = n / 2
            steps += 1
        else:
            n = (n * 3) + 1
            steps += 1
    return steps