from biniry_search import biniry_search
import time
import random
def expon_search(N, target):
    if N[0] == target:
        return 0
    index = 1
    while index < len(N) and N[index] <= target:
        index *= 2
    return biniry_search(N[:min(len(N), index)], target)



ns = list(range(8*200000))
tt = time.time()
n = expon_search(ns, 199000)
tt2 = time.time() - tt
print(f"Bites long: {ns.__sizeof__()}. Searched for: {tt2}. Index is: {n}")
