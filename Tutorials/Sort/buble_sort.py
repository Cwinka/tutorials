from random import shuffle
import time
def bubble_sort(arr):
    for i in range(len(arr)):
        # iterate through unplaced elements
        for idx in range(len(arr) - i - 1):
            if arr[idx] > arr[idx + 1]:
                # replacement
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]


unordered_list1 = list(range(8*497))
shuffle(unordered_list1)


tt = time.time()
bubble_sort(unordered_list1)
tt2 = time.time() - tt
print(f"Bites long: {unordered_list1.__sizeof__()}. Sorted for: {tt2}")
# O(N^2)
