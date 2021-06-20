from functools import lru_cache

# It's excellent!
def fibo(n):
    if type(n) != int or n <= 0:
        return print("This can only be integer and greater then 0")
    a, b = 0, 1
    for i in range(1, n + 1):
        b, a = a + b, b
        # print(i, ": ", a)
    return a
# print(fibo(500000))


# It's a terrible way
def fibo2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibo2(n - 1) + fibo2(n - 2)
# for i in range(1, 35):
#     print(i, ':', fibo2(i))

# But previous fibo can be cached using functools
@lru_cache(maxsize = 100)
def fibo2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibo2(n - 1) + fibo2(n - 2)
# for i in range(1, 101):
#     print(i, ':', fibo2(i))

#Here's another way how to write a good fibonacci using cach
fibonacci_cach = {}
def fibo2(n):
    #If "n" is already in the cach
    if n in fibonacci_cach:
        return fibonacci_cach[n]
    #Compute the N'th term
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n > 2:
        value = fibo2(n - 1) + fibo2(n - 2)
    #Cach the value and return it
    fibonacci_cach[n] = value
    return value
# for i in range(1, 1001):
#     print(i, ':', fibo2(i))

def fib3(n):
    def fib_iter(a, b, p, q, count):
        if count == 0:
            return b
        if count%2==0:
            return (fib_iter(a,
                            b,
                            p**2 + q**2,
                            2*p*q + q**2,
                            count/2))
        else:
            return fib_iter(b*q+a*q+a*p,
                            b*p+a*q,
                            p,
                            q,
                            count-1)
    return (fib_iter(1, 0, 0, 1, n))

# print(fib3(500000))



