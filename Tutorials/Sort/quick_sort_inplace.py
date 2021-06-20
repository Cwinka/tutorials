from random import randrange, shuffle
import time
def quicksort(list, start, end):
    # this portion of list has been sorted
    if start >= end:
        return
    # select random element to be pivot
    pivot_idx = randrange(start, end)
    pivot_element = list[pivot_idx]
    # swap random element with last element in sub-lists
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # we found an element out of place
        if list[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            # tally that we have one more lesser element
            less_than_pointer += 1
    # move pivot element to the right-most portion of lesser elements
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    # recursively sort left and right sub-lists
    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)

unordered_list1 = list(range(8*14000))
shuffle(unordered_list1)

tt = time.time()
quicksort(unordered_list1, 0 , len(unordered_list1)-1)
tt2 = time.time() - tt
print(f"Bites long: {unordered_list1.__sizeof__()}. Sorted for: {tt2}")

# O(N^2) OR O(NlogN) квадратичное вермя при подаче уже отсортированной последовательности (но не в такой имплементации с модулем рандом)
