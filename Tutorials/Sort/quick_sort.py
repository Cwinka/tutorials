from random import randint, shuffle
import time
def quicksort(s_list):
    if len(s_list) <= 1:
        return s_list
    smaller,equal,greater =[], [], []
    pivot = s_list[randint(0, len(s_list)-1)]
    for idx in range(len(s_list)):
        if s_list[idx] < pivot:    smaller.append(s_list[idx])
        elif s_list[idx] == pivot: equal.append(s_list[idx])
        else:                      greater.append(s_list[idx])
    return quicksort(smaller) + equal + quicksort(greater)


unordered_list1 = list(range(8*45000))
shuffle(unordered_list1)
tt = time.time()
quicksort(unordered_list1)
tt2 = time.time() - tt
print(f"Bites long: {unordered_list1.__sizeof__()}. Sorted for: {tt2}")
# O(N^2) OR O(NlogN) квадратичное вермя при подаче уже отсортированной последовательности (но не в такой имплементации с модулем рандом)
