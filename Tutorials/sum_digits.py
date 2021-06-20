def sum_digit(n):
    if n < 10:
        return n
    else:
        last_digit = n%10
        return last_digit + sum_digit(n//10)
