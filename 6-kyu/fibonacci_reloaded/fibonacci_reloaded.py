def fib(n):
    mem = 1
    prev_mem = 0
    
    if n == 1:
        return prev_mem
    if n == 2:
        return mem
    else:
        for number in range(3, n+1):
            actual_n = mem + prev_mem
            prev_mem = mem
            mem = actual_n
    return actual_n