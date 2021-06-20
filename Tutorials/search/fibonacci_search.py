def fibonacci_search(N, target):
    fib_minus_2, fib_minus_1 = 0, 1
    fib_m = fib_minus_1 + fib_minus_2
    while fib_m < len(N):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib_m
        fib_m = fib_minus_2 + fib_minus_1

    offset = -1
    while fib_m > 1:
        i = min(len(N)-1, offset+fib_minus_2)
        if N[i] < target:
            fib_m = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib_m - fib_minus_1

            offset = i
        elif N[i] > target:
            fib_m = fib_minus_2
            fib_minus_1  = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib_m - fib_minus_1
        else:
            return i

    if fib_minus_1 and N[offset] == target:
        return offset
    else:
        return -1




print(fibonacci_search(list(range(10000)), 500))
