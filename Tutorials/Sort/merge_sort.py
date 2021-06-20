from random import shuffle
import time
def merge_sort(items):
    if len(items) <= 1: # Base case. Остановка
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted) # возваращает лист из n элементов в left и right sorted, работает пока не восстановит весь лист

def merge(left, right):
    result = []
    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    if right:
        result += right
    return result

unordered_list1 = list(range(8*14000))
shuffle(unordered_list1)

tt = time.time()
merge_sort(unordered_list1)
tt2 = time.time() - tt
print(f"Bites long: {unordered_list1.__sizeof__()}. Sorted for: {tt2}")


#  O(N*logN) хуже quick sort потому что делает копию листа, из-за этого занимает больше памяти и времени
