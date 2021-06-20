import random

def simplisity_test(n, t=6):
    def simple(n):
        def expmod(base, exp, m):
            if exp == 0:
                return 1
            if exp%2==0:
                square = expmod(base, exp/2, m)
                res = (square**2)%m
                if 1 < square < n-1  and res==1:
                    return 0
                return res
            else:
                return (base*expmod(base, exp-1, m))%m
        if n <= 1:
            return False
        base = random.randint(1, n-1)
        if expmod(base, n-1, n)==1%n:
            return True
        else:
            return False
    check = 0
    for _ in range(t):
        if simple(n):
            check +=1
    return check == t

print(simplisity_test(101215541561561561))

